import subprocess

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
    subprocess.run("taskkill /f /im explorer.exe /t", shell=True, check=False)
    subprocess.Popen("%windir%\\explorer.exe", shell=True)
except Exception as e:
    print(f"{RED}Error: {e}{RESET}")


print(
    "\n Do you wanna restart?\n 1. Yes, Press (yes,y,yeah,yep)\n 2. Nope (nah,no,neh,n)"
)
userRestartInput = input(" >>> ").strip().lower()

if userRestartInput.startswith("y"):
    run_command("shutdown /r /t 5")
    print(f"{RED}System will be restarted in 5 Seconds!!{RESET}")
elif userRestartInput.startswith("n"):
    print(f"{GREEN}Thank you!!{RESET}")
    print("MADE BY: github.com/abdulrahmaninfra\n AKA: Lyenx")
    input("Press any key to exit")
else:
    print(f"Invalid input, Cancel restarting")
    print("MADE BY: github.com/abdulrahmaninfra\n AKA: Lyenx")
    input("Press any key to exit")
