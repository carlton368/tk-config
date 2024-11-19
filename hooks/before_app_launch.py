import os
import sys
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()

def execute(self, app_path, app_args, version, engine_path, **kwargs):
    """
    Before Unreal engine launch, add FBX module path to system path
    """
    self.logger.info("==================== HOOK START ====================")
    
    # bundle_cache에서 FBX 모듈 경로 가져오기 
    bundle_cache = os.path.join(
        os.getenv('APPDATA'),
        'Shotgun',
        'bundle_cache',
        'gitbranch',
        'tk-config.git',
        'e4a5448',  # 현재 커밋 해시
        'hooks',
        'packages',
        'win'
    )
    
    self.logger.info(f"Bundle cache path: {bundle_cache}")
    if os.path.exists(bundle_cache):
        self.logger.info(f"Adding FBX module path: {bundle_cache}")
        sys.path.append(bundle_cache)
        
        # PYTHONPATH에도 추가
        paths = os.environ.get('PYTHONPATH', '').split(os.pathsep)
        if bundle_cache not in paths:
            paths.append(bundle_cache)
            os.environ['PYTHONPATH'] = os.pathsep.join(paths)
    else:
        self.logger.warning(f"FBX module path does not exist: {bundle_cache}")
    
    self.logger.info("sys.path after update:")
    self.logger.info("\n".join(sys.path))
    
    self.logger.info("==================== HOOK END ====================")
    
    result = super(UnrealEngineStartup, self).execute(
        app_path,
        app_args,
        version,
        engine_path,
        **kwargs
    )
    
    return result