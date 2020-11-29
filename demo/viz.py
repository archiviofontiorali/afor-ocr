import holoviews as hv
import numpy as np
import ocr.io

try:
    import holoviews.operation.datashader
except ModuleNotFoundError:
    RASTER_AVAILABLE = False
else:
    RASTER_AVAILABLE = True


def hv_image(image: np.ndarray, raster: bool = True, with_border=False):
    """Create an image bokeh plot with right shapes and aspect ratio."""
    width, height = image.shape[1], image.shape[0]
    bounds = (0, 0, width, height)
    if image.ndim == 3 and image.shape[2] == 3:
        plot = hv.RGB(image, bounds=bounds)
    else:
        plot = hv.Image(image, bounds=bounds)

    if with_border:
        size = max(width, height)
        pad_x = (size - width) // 2
        pad_y = (size - height) // 2
        plot = plot.opts(
            aspect=1,
            xlim=(-pad_x, max(width, height) - pad_x),
            ylim=(-pad_y, max(width, height) - pad_y),
        )
    else:
        plot = plot.opts(aspect=ocr.io.aspect_ratio(image))

    if raster and RASTER_AVAILABLE:
        return holoviews.operation.datashader.rasterize(plot)
    return plot
