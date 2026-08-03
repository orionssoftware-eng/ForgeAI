from forge.plugins.base import Plugin, Capability


class BlenderPlugin(Plugin):

    name = "Blender"

    version = "1.0"

    capabilities = [

        Capability(
            "3d_modeling",
            "Create and edit meshes"
        ),

        Capability(
            "materials",
            "Materials and shaders"
        ),

        Capability(
            "rendering",
            "Rendering"
        ),

        Capability(
            "animation",
            "Animation"
        )

    ]

    def initialize(self):

        print("✓ Blender Plugin initialized")