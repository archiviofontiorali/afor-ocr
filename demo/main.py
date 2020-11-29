import pathlib
from collections import OrderedDict
from typing import List, Tuple

import holoviews as hv
import holoviews.streams
import numpy as np
import panel as pn
import param

import ocr.io
import ocr.preprocessing
import ocr.tesseract

from .viz import hv_image


def disable_logo(plot, _element):
    plot.state.toolbar.logo = None


hv.extension("bokeh")
hv.opts.defaults(
    hv.opts.Image(),
    hv.opts.RGB(
        responsive=True, axiswise=True, xaxis="bare", yaxis="bare", bgcolor="black"
    ),
    hv.opts.Rectangles(active_tools=["box_edit"], fill_alpha=0.5),
)
pn.extension()


class Demo(param.Parameterized):
    select_image = param.ObjectSelector(objects=[None])

    btn_convert = param.Action(lambda e: e.ocr_convert(), label="OCR")
    btn_reset = param.Action(lambda e: e.reset(), label="Reset")

    brightness = param.Number(1.0, bounds=(0.0, 1.0))
    saturation = param.Number(1.0, bounds=(0.0, 1.0))
    angle = param.Integer(0, bounds=(-45, 45))
    orientation = param.Selector(objects=[0, -90, +90, 180])

    def __init__(self, images: List[Tuple[str, np.ndarray]]):
        super().__init__()
        self._images = OrderedDict(images)
        self.param["select_image"].objects = self._images.keys()
        self.param["select_image"].default = images[0][0]

        self._orig = images[0][1]
        self.image = self._orig.copy()

        self.boxes = hv.Rectangles([])
        self.box_stream = hv.streams.BoxEdit(source=self.boxes, num_objects=1)

        self.converter = ocr.tesseract.Tesseract(lang="ita+ita_old")
        self._text = ""

    @property
    def box(self):
        height, width = self.image.shape[:2]
        if self.box_stream.data:
            x0 = max(int(self.box_stream.data["x0"][0]), 0)
            x1 = min(int(self.box_stream.data["x1"][0]), width)
            y0 = max(height - int(self.box_stream.data["y1"][0]), 0)
            y1 = min(height - int(self.box_stream.data["y0"][0]), height)
        else:
            x0, y0, x1, y1 = 0, 0, width, height
        return x0, y0, x1, y1

    @param.depends("select_image", watch=True)
    def change_image(self):
        self._orig = self._images[self.select_image]
        self.image = self._orig.copy()
        self.reset()

    def reset(self):
        self._text = ""
        self.angle = self.param["angle"].default
        self.orientation = self.param["orientation"].default
        self.brightness = self.param["brightness"].default
        self.saturation = self.param["saturation"].default
        self.param.trigger("btn_reset")

    def ocr_convert(self):
        image = ocr.preprocessing.crop(self.image, *self.box)
        text = self.converter.convert(image)
        text = text.strip().replace("\n", " ")
        self._text = text if text else "No text found"
        self.param.trigger("btn_convert")

    @param.depends("angle", "orientation", "brightness", "saturation", watch=True)
    def update_image(self):
        self._text = ""
        angle = self.angle + self.orientation
        image = ocr.preprocessing.rotate(self._orig, angle, with_bounds=True)
        image = ocr.preprocessing.change_brightness(image, self.brightness)
        image = ocr.preprocessing.change_saturation(image, self.saturation)
        self.image = image

    @param.depends("btn_convert", "btn_reset", "image")
    def view(self):
        plot = hv_image(self.image, with_border=True) * self.boxes
        plot = plot.opts(plot=dict(hooks=[disable_logo]))

        grid = pn.GridSpec(sizing_mode="stretch_both")
        grid[0, :] = pn.Spacer()
        grid[1:12, 0] = pn.Spacer()
        grid[1:12, 12] = pn.Spacer()
        grid[12, :] = pn.Spacer()

        grid[1:12, 1:7] = plot
        grid[1:6, 7:12] = pn.Param(
            app.param, widgets={"orientation": pn.widgets.RadioButtonGroup}
        )
        grid[6:12, 7:12] = pn.pane.Markdown(
            "## Text\n" + self._text,
            margin=25,
            style={"font-size": "1.5em"},
            max_height=300,
        )

        return grid


_images = []
for ext in ("png", "jpg"):
    for path in sorted(pathlib.Path("images").glob(fr"*.{ext}")):
        im = ocr.io.load_image(path)
        _images.append((path.name[:-4], im))
_images.append(("opencv", ocr.io.create_example_image((256, 256), text="OpenCV")))

app = Demo(_images)

main = pn.Row(app.view, width=1900, height=1060)
main.servable()
