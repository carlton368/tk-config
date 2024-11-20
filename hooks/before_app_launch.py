import os
import sys
import sgtk

HookBaseClass = sgtk.get_hook_baseclass()

class BeforeAppLaunch(HookBaseClass):

    def execute(self, app_path, app_args, version, engine_name, software_entity=None, **kwargs):
        """
        언리얼 엔진 시작 전에 Python 경로를 설정합니다.
        """
        if engine_name == "tk-unreal":
            # 추가할 경로들
            external_paths = [
                "external_path1",
                "external_path2"
            ]
            
            # 새로운 경로들을 세미콜론으로 결합
            new_paths = os.pathsep.join(external_paths)
            
            # PYTHONPATH 설정
            if 'PYTHONPATH' in os.environ:
                os.environ['PYTHONPATH'] += os.pathsep + new_paths
            else:
                os.environ['PYTHONPATH'] = new_paths
                
            # UE_PYTHONPATH 설정
            if 'UE_PYTHONPATH' in os.environ:
                os.environ['UE_PYTHONPATH'] += os.pathsep + new_paths
            else:
                os.environ['UE_PYTHONPATH'] = new_paths
            
            if 'WONJIN_BEFORE_LAUNCH' in os.environ:
                os.environ['WONJIN_BEFORE_LAUNCH'] += os.pathsep + 'WONJIN_BEFORE_LAUNCH'
            else:
                os.environ['WONJIN_BEFORE_LAUNCH'] = 'WONJIN_BEFORE_LAUNCH'

            # 로깅
            self.parent.log_debug("WONJIN_BEFORE_APP_LAUNCH Updated Python paths:")
            self.parent.log_debug("PYTHONPATH: %s" % os.environ['PYTHONPATH'])
            self.parent.log_debug("UE_PYTHONPATH: %s" % os.environ['UE_PYTHONPATH'])
            self.parent.log_debug("WONJIN_BEFORE_LAUNCH: %s" % os.environ['WONJIN_BEFORE_LAUNCH2'])
            self.parent.log_debug("sys.path: %s" % sys.path)

        # 상위 클래스의 execute 실행
        return super(BeforeAppLaunch, self).execute(
            app_path, 
            app_args, 
            version,
            engine_name,
            software_entity,
            **kwargs
        )