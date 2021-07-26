import panel as pn
from bokeh.themes import Theme as _BkTheme
from panel.template.theme import Theme

AnacondaColors = ['#43b049', '#C2D500', '#006A5B', '#0075A9']


class AnacondaTheme(Theme):

    bokeh_theme = _BkTheme(filename='assets/bokeh_theme.yaml')


class BootstrapAnacondaTheme(AnacondaTheme):

    _template = pn.template.BootstrapTemplate


class MaterialAnacondaTheme(AnacondaTheme):

    _template = pn.template.MaterialTemplate
