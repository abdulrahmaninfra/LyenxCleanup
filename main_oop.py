import subprocess
import time
import os 
from colorama import Fore

class Cleanup:
    def __init__(self, name: str,command: str, commands: list):
        self.name = name
        self.command = command
        self.is_complate = False
        self.error_msg = None
        self.commands = commands

    def _load_default_coomands(self):
        self.commands = [
            'del /f /s /q "%windir%\\Prefetch\\*.*"',
            'rd /s /q "%windir%\\Temp"',
            'md "%windir%\\Temp"',
            'rd /s /q "%temp%"',
            'md "%temp%"',
            'rd /s /q "%LocalAppData%\\Microsoft\\Windows\\INetCache"',
            "rd /s /q %systemdrive%\\$Recycle.Bin",
            "del /f /s /q %systemdrive%\\*.tmp",
            "del /f /s /q %systemdrive%\\*_mp",
            "del /f /s /q %systemdrive%\\*.gid",
            "del /f /s /q %systemdrive%\\*.chk",
            "ipconfig /flushdns",
            "cleanmgr /sagerun:1", 
        ]

    def execute(self):
        try:
            run = subprocess.run(self.command, shell=True, check=True,stdout=subprocess.DEVNULL , stderr=subprocess.PIPE)

            if run.returncode == 0:
                print(f"{Fore.GREEN}Executed: {self.command}{Fore.RESET}")
                self.is_complate = True 
                return True
            else:
                self.error_msg = run.stderr
                print(f"{Fore.RED}Error occurred while executing: {self.command}{Fore.RESET}")
                return False
            
        except Exception as e:
            self.error_msg = str(e)
            print(f"{Fore.RED}Exception occurred: {e}{Fore.RESET}")
            return False
