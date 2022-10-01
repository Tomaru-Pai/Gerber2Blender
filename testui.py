# https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui

import bpy
import os

from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

# B2G = Blender to Gerber
class B2G:
    # Window where the Panel is located. In this case on the 3D Viewing Area
    bl_space_type = "VIEW_3D"
    # Location where the Panel is displayed
    bl_region_type = "UI"
    # Sets Category Bar where the Panel is displayed, when the Region does't already exist, a new with the set name will be displayed
    bl_category = "B2G"
    # When Blender is started the ToolBox will not open
    bl_options = {"DEFAULT_CLOSED"}

class B2G_Import_Gerber(B2G, bpy.types.Panel):
    bl_idname = "Import Gerber"
    bl_label = "Import Gerber"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Import your .gbr File here!")
        
        
class Import_Field(Operator, ImportHelper):
    bl_idname = "test.open_filebrowser"
    bl_label = "Open the file browser (yay)"
    
    filter_glob: StringProperty(
        default='*.gbr',
        options={'HIDDEN'}
    )
    
    some_boolean: BoolProperty(
        name='Do a thing',
        description='Do a thing with the file you\'ve selected',
        default=True,
    )

    def execute(self, context):
        """Do something with the selected file(s)."""

        filename, extension = os.path.splitext(self.filepath)
        
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        print('Some Boolean:', self.some_boolean)
        
        return {'FINISHED'}

classes = (
    B2G_Import_Gerber,
    Import_Field
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__" :
    register()
    
    
    #Test import
    bpy.ops.test.open_filebrowser('INVOKE_DEFAULT')
