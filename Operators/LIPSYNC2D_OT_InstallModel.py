from typing import Literal
import bpy
from bpy.types import Context

from ..Preferences.LIPSYNC2D_AP_Preferences import LIPSYNC2D_VoskHelper
from ..LIPSYNC2D_Utils import get_package_name

class LIPSYNC2D_OT_InstallModel(bpy.types.Operator):
    bl_idname = "wm.lipsync_install_model"
    bl_label="Download Model"
    bl_description="Download and install the selected language model"

    def execute(self, context: Context) -> set[Literal['RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH', 'INTERFACE']]:
        prefs = context.preferences.addons[get_package_name()].preferences
        try:
            LIPSYNC2D_VoskHelper.install_model(prefs, context)
        except Exception as e:
            self.report({'ERROR'}, f"Unable to install model: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, "Model download started...")
        return {'FINISHED'}
