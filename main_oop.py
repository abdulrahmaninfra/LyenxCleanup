import subprocess
import time
import os 


class Cleanup:
    def __init__(self, name: str,command: str):
        self.name = name
        self.command = command

    def execute(self):
        try:
            subprocess.run(self.command, shell=True, check=True)
        except Exception as cleanup_execute_error:
            return self.cleanup_execute_error



class WinCleaner:
    def __init__(self,tasks):
        self.tasks= []

    def _default_commands(self):
        commands = [
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
    "cleanmgr /sagerun:1",]

    commands_dict = {
    "clear_prefetch": 'del /f /s /q "%windir%\\Prefetch\\*.*"',
    "delete_system_temp": 'rd /s /q "%windir%\\Temp"',
    "recreate_system_temp": 'md "%windir%\\Temp"',
    "delete_user_temp": 'rd /s /q "%temp%"',
    "recreate_user_temp": 'md "%temp%"',
    "clear_inet_cache": 'rd /s /q "%LocalAppData%\\Microsoft\\Windows\\INetCache"',
    "empty_recycle_bin": "rd /s /q %systemdrive%\\$Recycle.Bin",
    "remove_tmp_files": "del /f /s /q %systemdrive%\\*.tmp",
    "remove_mp_files": "del /f /s /q %systemdrive%\\*_mp",
    "remove_gid_files": "del /f /s /q %systemdrive%\\*.gid",
    "remove_chk_files": "del /f /s /q %systemdrive%\\*.chk",
    "flush_dns": "ipconfig /flushdns",
    "run_cleanmgr": "cleanmgr /sagerun:1",
}