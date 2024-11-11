import sys
import os
import sgtk

class PythonInterpreter(sgtk.hook.Hook):
    """
    Hook that specifies the Python interpreter to use for tk-multi-pythonconsole
    """    
    def execute(self, **kwargs):
        """
        Return the path to Python 3.7 interpreter from Miniconda3
        
        :returns: Path to Python interpreter
        :rtype: str
        """
        # Miniconda3 Python 3.7 env path
        if sys.platform == "win32":
            python_path = r"C:\Users\lee\miniconda3\envs\py37\python.exe"
            
            # Try alternate path if not found
            if not os.path.exists(python_path):
                python_path = os.path.expanduser("~/miniconda3/envs/py37/python.exe")
        
        # Check if Python exists
        if not os.path.exists(python_path):
            self.logger.warning(
                "Python 3.7 interpreter '%s' does not exist!" % python_path
            )
            return None
            
        return python_path