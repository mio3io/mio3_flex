import bpy
from bpy.types import AddonPreferences
from bpy.props import BoolProperty, FloatProperty, FloatVectorProperty, IntProperty, StringProperty, EnumProperty
from . import main_ui


class PREFERENCE_mio3me(AddonPreferences):
    bl_idname = __package__

    def update_category(self, context):
        main_ui.reregister()

    category: StringProperty(
        name="Category",
        default="Mio3",
        update=update_category,
    )

    use_density: BoolProperty(
        name="Auto Density",
        description="Automatically adjust control point distribution based on edge density",
        default=True,
    )
    show_original_edge: BoolProperty(
        name="Show Original Edge",
        description="Display the original edge loop for reference",
        default=True,
    )
    right_click_action: EnumProperty(
        name="Right Click Action",
        description="Choose the action for the right mouse button",
        items=[
            ('CONFIRM', "Confirm", "Use right mouse button to confirm actions"),
            ('CANCEL', "Cancel", "Use right mouse button to cancel actions"),
        ],
        default='CANCEL',
    )

    col_spline_default: FloatVectorProperty(
        name="Default",
        subtype="COLOR_GAMMA",
        size=4,
        default=(0.0, 0.7, 1.0, 1.0),
        min=0.0,
        max=1.0,
    )
    col_spline_active: FloatVectorProperty(
        name="Active",
        subtype="COLOR_GAMMA",
        size=4,
        default=(0.0, 0.7, 1.0, 1.0),
        min=0.0,
        max=1.0,
    )
    col_point_default: FloatVectorProperty(
        name="Default",
        subtype="COLOR_GAMMA",
        size=4,
        default=(0.36, 0.79, 1.00, 1.0),
        min=0.0,
        max=1.0,
    )
    col_point_active: FloatVectorProperty(
        name="Active",
        subtype="COLOR_GAMMA",
        size=4,
        default=(0.85, 0.85, 0.85, 1.0),
        min=0.0,
        max=1.0,
    )
    col_point_selected: FloatVectorProperty(
        name="Selected",
        subtype="COLOR_GAMMA",
        size=4,
        default=(0.85, 0.85, 0.85, 1.0),
        min=0.0,
        max=1.0,
    )
    col_edge_original: FloatVectorProperty(
        name="Original Edge",
        subtype="COLOR_GAMMA",
        size=4,
        default=(0.40, 0.54, 0.36, 1.0),
        min=0.0,
        max=1.0,
    )
    point_size_default: IntProperty(name="Default", default=8, min=4)
    point_size_active: IntProperty(name="Active", default=10, min=4)
    point_size_selected: IntProperty(name="Selected", default=10, min=4)

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = False

        col = layout.column()
        col.use_property_split = True
        col.prop(self, "category")
        row = col.row()
        row.prop(self, "right_click_action", expand=True)

        layout.label(text="Display", icon="COLOR")
        col = layout.column()
        col.use_property_split = True
        col.label(text="Spline", icon="IPO_EASE_IN_OUT")
        col.prop(self, "col_spline_default")
        col.prop(self, "col_spline_active")
        col.prop(self, "col_edge_original")

        col = layout.column()
        col.use_property_split = True
        col.label(text="Point", icon="SNAP_MIDPOINT")
        row = col.row(align=True)
        row.prop(self, "col_point_default", text="Default")
        row.prop(self, "point_size_default", text="Size")
        row = col.row(align=True)
        row.prop(self, "col_point_active", text="Active")
        row.prop(self, "point_size_active", text="Size")
        row = col.row(align=True)
        row.prop(self, "col_point_selected", text="Selected")
        row.prop(self, "point_size_selected", text="Size")


def register():
    bpy.utils.register_class(PREFERENCE_mio3me)


def unregister():
    bpy.utils.unregister_class(PREFERENCE_mio3me)
