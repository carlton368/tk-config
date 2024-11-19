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
            # 외부 Python 모듈 경로 설정
            external_paths = [
                "C:/Python/Lib/site-packages",  # pip로 설치한 패키지들
                "C:/Users/admin/AppData/Local/Programs/Python/Python39/Lib/site-packages",  # 추가 파이썬 패키지
                # 필요한 다른 경로들 추가
            ]

            # 현재 PYTHONPATH 가져오기
            current_pythonpath = os.environ.get('PYTHONPATH', '').split(os.pathsep)
            
            # 새로운 경로 추가
            for path in external_paths:
                if os.path.exists(path) and path not in current_pythonpath:
                    current_pythonpath.append(path)
                    if path not in sys.path:
                        sys.path.append(path)
            
            # 환경 변수 업데이트
            os.environ['PYTHONPATH'] = os.pathsep.join(current_pythonpath)
            os.environ['UE_PYTHONPATH'] = os.environ['PYTHONPATH']

            # 로깅
            self.parent.log_debug("Updated Python paths:")
            self.parent.log_debug("PYTHONPATH: %s" % os.environ['PYTHONPATH'])
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