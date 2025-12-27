from . import preferences
from . import translation
from . import main_ui
from .modules import curve_edges


module_list = [
    preferences,
    translation,
    curve_edges,
    main_ui,
]


def register():
    for module in module_list:
        module.register()


def unregister():
    for module in reversed(module_list):
        module.unregister()
