import subprocess
import time

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def run_command(command):
    subprocess.run(command, shell=True, check=True)


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
    "cleanmgr /autoclean",
]

for cmd in commands:
    try:
        run_command(cmd)
        print(f"{GREEN}Executed: {cmd}{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")


print(f"{GREEN}Restarting Windows Explorer!{RESET}")
try:
    subprocess.run("taskkill /f /im explorer.exe", shell=True, check=False)
    time.sleep(2)
    subprocess.Popen("%windir%\\explorer.exe", shell=True)
except Exception as e:
    print(f"{RED}Error: {e}{RESET}")


print(
    f"\n Do you wanna restart Windows?\n    1. {GREEN}Yes{RESET}\n    2. {RED}No{RESET}"
)
userRestartInput = input(" >>> ").strip().lower()

if userRestartInput.startswith("y") or userRestartInput == "1":
    run_command("shutdown /r /t 5")
    print(f"{RED}System will be restarted in 5 Seconds!!{RESET}")

elif userRestartInput.startswith("n") or userRestartInput == "2":
    print(f"{GREEN}Thank you!!{RESET}")
    print("MADE BY: github.com/abdulrahmaninfra\nAKA: Lyenx")
    input("Press any key to exit")

else:
    print(f"Invalid input, Cancel restarting")
    print("MADE BY: github.com/abdulrahmaninfra\nAKA: Lyenx")
    input("Press any key to exit")
