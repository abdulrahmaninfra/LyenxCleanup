import subprocess
import time
import os 


class Cleanup:
    def __init__(self, name: str,command: str):
        self.name = name
        self.command = command
        self.is_complate = False
        self.error_msg = None

    def execute(self):
        try:
            run = subprocess.run(self.command, shell=True, check=True,stdout=subprocess.DEVNULL , stderr=subprocess.PIPE)

            if run.returncode == 0:
                self.is_complate = True
                return True
            else:
                self.error_msg = run.stderr
                return False
            
        except Exception as e:
            self.error_msg = str(e)
            return False
