# LyenxCleanup

A lightweight Windows system cleanup utility that removes temporary files, caches, and unnecessary data to free up disk space and improve system performance.

## Features

- **Prefetch Cleanup**: Removes Windows Prefetch files to recover space
- **Temp Folder Cleanup**: Clears both system and user temporary directories
- **Internet Cache Removal**: Deletes INetCache files from Windows AppData
- **Recycle Bin Emptying**: Permanently removes all files from Recycle Bin
- **Temporary File Removal**: Eliminates `.tmp`, `.chk`, `.gid` files across the system drive
- **DNS Cache Flush**: Clears DNS resolver cache for improved network performance
- **Disk Cleanup Manager**: Runs Windows automated cleanup utility
- **Windows Explorer Restart**: Safely restarts Windows Explorer after cleanup
- **Optional System Restart**: User-prompted option to restart Windows

## Requirements

- Windows 7 or later
- Python 3.x
- Administrator privileges (required for system file operations)

## Installation

### From Release
Download the latest executable from the [Releases](https://github.com/abdulrahmaninfra/LyenxCleanup/releases) page and run it directly.

### From Source
1. Clone the repository:
```bash
git clone https://github.com/abdulrahmaninfra/LyenxCleanup.git
cd LyenxCleanup
```

2. Run with Python (administrator mode required):
```bash
python main.py
```

## Usage

1. **Run as Administrator**: Right-click `LyenxCleanup.exe` (or `main.py`) and select "Run as administrator"
2. **Automatic Cleanup**: The script will automatically execute all cleanup operations
3. **System Restart Prompt**: After cleanup completes, you'll be asked if you want to restart Windows
   - Enter `Y` or `1` to restart (5-second countdown)
   - Enter `N` or `2` to skip restart

## What Gets Cleaned

| Location | Files Removed |
|----------|---|
| `%windir%\Prefetch` | Prefetch cache files |
| `%windir%\Temp` | System temporary files |
| `%temp%` | User temporary files |
| `%LocalAppData%\Microsoft\Windows\INetCache` | Internet Explorer/Edge cache |
| `$Recycle.Bin` | Recycle Bin contents |
| System Drive Root | `.tmp`, `.chk`, `.gid`, `*_mp` files |
| DNS Cache | Cached DNS resolver entries |

## Safety Notes

⚠️ **Important**: This tool performs aggressive system cleanup operations:
- **Back up important files** before running
- Requires **administrator privileges**
- Some operations cannot be undone
- May require system restart to complete
- Temporarily restarts Windows Explorer (safe operation)

## Command-Line Operations

The script uses these Windows commands:
- `del` - Delete files recursively
- `rd` - Remove directories recursively
- `ipconfig /flushdns` - Clear DNS cache
- `cleanmgr` - Automated Windows cleanup
- `taskkill` - Restart Explorer process
- `shutdown` - Initiate system restart

## Building from Source

To build the executable from source:
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --console --icon "icon.ico" --name "Lyenx Cleanup" --uac-admin "main.py"
```

The compiled executable will be in the `dist` folder.

## Version History

See [Releases](https://github.com/abdulrahmaninfra/LyenxCleanup/releases) for version history and download links.

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs via [Issues](https://github.com/abdulrahmaninfra/LyenxCleanup/issues)
- Submit pull requests with improvements
- Suggest new cleanup operations

## License

This project is open source and available under the MIT License.

## Credits

**Author**: [abdulrahmaninfra](https://github.com/abdulrahmaninfra) (Lyenx)

## Disclaimer

This tool is provided as-is. The author is not responsible for any data loss or system issues that may occur from its use. Always ensure you have backups before running system cleanup utilities.

---

**Use responsibly!** 🧹