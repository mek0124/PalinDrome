#!/usr/bin/env python3
"""
Build script that creates standalone executables for all platforms.
Generates executables for the current platform and warns about others.
"""
import os
import sys
import platform
import subprocess
import shutil
import tarfile
from pathlib import Path

def build_for_current_platform():
    current_system = platform.system()
    print(f"Building for current platform: {current_system}")

    # Clean previous builds
    for folder in ['dist', 'build']:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    # Platform-specific configurations
    is_windows = current_system == "Windows"
    is_mac = current_system == "Darwin"
    is_linux = current_system == "Linux"

    # Base PyInstaller command
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--clean',
        '--noconfirm',
        '--windowed',
        '--name=PalinDrome',
        '--add-data=src/main_window.ui:src',
        '--add-data=app-icon.jpeg:.',
        '--icon=app.ico',
        '--hidden-import=PySide6.QtCore',
        '--hidden-import=PySide6.QtGui',
        '--hidden-import=PySide6.QtWidgets',
        'src/app/main.py'
    ]

    if is_windows:
        cmd.extend(['--onefile', '--noconsole'])
        # Windows needs semicolons in add-data
        for i, arg in enumerate(cmd):
            if arg.startswith('--add-data='):
                cmd[i] = arg.replace(':', ';')
    elif is_mac:
        cmd.extend([
            '--osx-bundle-identifier=com.yourcompany.palindrome',
            '--windowed'  # Proper .app bundle
        ])
    else:  # Linux
        cmd.extend(['--onefile'])

    # Run PyInstaller
    subprocess.run(cmd, check=True)

    # Package the output
    if is_windows:
        package_windows()
    elif is_mac:
        package_mac()
    else:
        package_linux()

    # Warn about other platforms
    other_platforms = {
        "Windows": is_windows,
        "macOS": is_mac,
        "Linux": is_linux
    }
    print("\nNote about cross-platform building:")
    for platform_name, is_current in other_platforms.items():
        if not is_current:
            print(f"- {platform_name} builds must be created on a {platform_name} system")

def package_windows():
    """Package Windows .exe into a zip"""
    exe_path = Path('dist') / 'PalinDrome.exe'
    if exe_path.exists():
        shutil.make_archive('PalinDrome-Windows', 'zip', 'dist')
        print("Created PalinDrome-Windows.zip")

def package_mac():
    """Package Mac .app into a zip"""
    app_path = Path('dist') / 'PalinDrome.app'
    if app_path.exists():
        # Create a simple command script
        with open('dist/Run_PalinDrome.command', 'w') as f:
            f.write("#!/bin/sh\n")
            f.write(f'open "{app_path}"\n')
        os.chmod('dist/Run_PalinDrome.command', 0o755)
        
        # Zip both the app and the command script
        shutil.make_archive('PalinDrome-macOS', 'zip', 'dist')
        print("Created PalinDrome-macOS.zip")

def package_linux():
    """Package Linux executable into a tar.gz"""
    bin_path = Path('dist') / 'PalinDrome'
    if bin_path.exists():
        # Create a simple run script
        with open('dist/run_palindrome.sh', 'w') as f:
            f.write("#!/bin/sh\n")
            f.write(f'DIR="$( cd "$( dirname "$0" )" && pwd )"\n')
            f.write('"$DIR/PalinDrome" "$@"\n')
        os.chmod('dist/run_palindrome.sh', 0o755)
        
        # Create tar.gz
        with tarfile.open('PalinDrome-Linux.tar.gz', 'w:gz') as tar:
            tar.add('dist/PalinDrome', arcname='PalinDrome')
            tar.add('dist/run_palindrome.sh', arcname='run_palindrome.sh')
        print("Created PalinDrome-Linux.tar.gz")

if __name__ == "__main__":
    try:
        import tarfile
    except ImportError:
        print("Error: tarfile module not found")
        sys.exit(1)
        
    build_for_current_platform()