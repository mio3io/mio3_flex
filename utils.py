import bpy

DEBUG = False


def is_local_obj(obj):
    return obj is not None and obj.library is None and obj.override_library is None


def check_register(cls):
    is_exist = hasattr(bpy.types, cls.__name__)
    if not is_exist:
        try:
            bpy.utils.register_class(cls)
        except:
            print("Failed to register class: {}".format(cls.__name__))


def check_unregister(cls):
    is_exist = hasattr(bpy.types, cls.__name__)
    if is_exist:
        try:
            bpy.utils.unregister_class(cls)
        except:
            print("Failed to unregister class: {}".format(cls.__name__))


def redraw_3d_views(context):
    for area in context.screen.areas:
        if area.type == "VIEW_3D":
            area.tag_redraw()


# def linear_rgb_to_srgb(rgb):
#     return Color(rgb).from_scene_linear_to_srgb()

