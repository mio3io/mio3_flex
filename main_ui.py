import bpy
from bpy.types import Panel, PropertyGroup
from bpy.props import BoolProperty, FloatProperty, IntProperty, PointerProperty
from .utils import is_local_obj, check_unregister, check_register
from .globals import get_preferences


class MIO3_PT_flex(Panel):
    bl_label = "Mio3 Flex"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Mio3"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return is_local_obj(obj) and obj.mode == "EDIT"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=False)
        split = col.split(factor=0.7, align=True)
        split.operator("mesh.mio3_curve_edges")
        split.operator("mesh.mio3_curve_edges_quick", text="Quick")
        split = col.split(factor=0.6, align=True)
        split.label(text="Control Points", icon="HANDLE_ALIGNED")
        split.prop(context.window_manager.mio3ce, "control_num", text="")

        split = col.split(factor=0.6, align=True)
        split.label(text="Roundness", icon="SMOOTHCURVE")
        split.prop(context.window_manager.mio3ce, "clamp", text="")


class MIO3_PG_flex(PropertyGroup):
    control_num: IntProperty(name="Control Points", description="[Ctrl] + Wheel", default=3, min=2, max=30)
    clamp: FloatProperty(name="Clamp", description="[Ctrl] + [Shift] + Wheel", default=1.2, min=0, max=2, step=5)
    hide_ui: BoolProperty(name="Hide UI", default=False, options={"SKIP_SAVE"})


classes = [
    MIO3_PG_flex,
    MIO3_PT_flex,
]


def register():
    prefs = get_preferences()
    for cls in classes:
        if hasattr(cls, "bl_category"):
            cls.bl_category = prefs.category
        check_register(cls)

    bpy.types.WindowManager.mio3ce = PointerProperty(type=MIO3_PG_flex)


def unregister():
    for cls in reversed(classes):
        check_unregister(cls)

    del bpy.types.WindowManager.mio3ce


def reregister():
    unregister()
    register()
