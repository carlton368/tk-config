import sys
import os
import sgtk

class PythonInterpreter(sgtk.hook.Hook):
    """
    Hook that specifies the Python interpreter to use for tk-multi-pythonconsole
    """    
    def execute(self, **kwargs):
        """
        Return the path to Python 3.7 interpreter and append to sys.path
        
        :returns: Path to Python interpreter
        :rtype: str
        """
        # Miniconda3 Python 경로들
        python_paths = [
            r"C:\Users\lee\miniconda3\envs\py37",  # Python 실행 파일 폴더
            r"C:\Users\lee\miniconda3\envs\py37\Lib\site-packages",  # 사이트 패키지
            r"C:\Users\lee\miniconda3\envs\py37\Lib",  # 표준 라이브러리
            r"C:\Users\lee\miniconda3\envs\py37\DLLs"  # DLL 파일들
        ]
        
        # sys.path에 경로 추가
        for path in python_paths:
            if os.path.exists(path) and path not in sys.path:
                sys.path.append(path)
                self.logger.info(f"Added to sys.path: {path}")
        
        # Python 실행 파일 경로 반환
        python_exe = os.path.join(python_paths[0], "python.exe")
        
        if not os.path.exists(python_exe):
            self.logger.warning(
                f"Python interpreter not found at: {python_exe}"
            )
            return None
            
        self.logger.info(f"Using Python interpreter: {python_exe}")
        self.logger.info(f"Updated sys.path: {sys.path}")
            
        return python_exe