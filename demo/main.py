import holoviews as hv
import panel as pn

from . import __version__
from .demo import DemoApp
from .images import create_sample_image, load_from_folder

# Initialize Holoviews and Panel
hv.extension("bokeh")
hv.opts.defaults(
    hv.opts.Image(),
    hv.opts.RGB(
        responsive=True, axiswise=True, xaxis="bare", yaxis="bare", bgcolor="black"
    ),
    hv.opts.Rectangles(active_tools=["box_edit"], fill_alpha=0.5),
)
pn.extension()

# Print version
print("Package version:", __version__)

# Load images
images = []
images.extend(load_from_folder("images"))
images.append(create_sample_image())

# Create demo app
demo = DemoApp(images, name="Demo")

# Initialize Panel app
app = pn.Row(demo.view, width=1280, height=1080)
app.servable()
