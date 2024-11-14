import os
import sys
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()

class UnrealEngineStartup(HookBaseClass):
    def execute(self, app_path, app_args, version, engine_path, **kwargs):
        """
        Before Unreal engine launch, add FBX module path to system path
        
        :param app_path: Path to application being launched
        :param app_args: Command line arguments to pass to application
        :param version: Version of application being launched
        :param engine_path: Path to engine root directory
        """
        
        # Get the current bundle
        self.logger.debug("Executing custom Unreal startup hook...")
        
        # Get the path to the hooks/packages/win directory
        current_engine = self.parent.engine
        config_root = current_engine.sgtk.pipeline_configuration.get_path()
        fbx_module_path = os.path.join(
            config_root,
            "hooks",
            "packages",
            "win"
        )
        
        # Add the FBX module path to system path if it exists
        if os.path.exists(fbx_module_path):
            self.logger.debug("Adding FBX module path: %s" % fbx_module_path)
            sys.path.append(fbx_module_path)
        else:
            self.logger.warning("FBX module path does not exist: %s" % fbx_module_path)
            
        # Execute the default hook
        result = super(UnrealEngineStartup, self).execute(
            app_path, 
            app_args, 
            version,
            engine_path, 
            **kwargs
        )
        
        return result