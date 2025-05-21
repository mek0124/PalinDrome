#!/usr/bin/env python3
"""
Build script for PalindromeChecker application
This script handles the PyInstaller build process with proper configuration
to avoid OpenSSL and Kerberos-related issues.
"""

import os
import sys
import subprocess
import shutil

def main():
    print("Building PalinDrome application...")

    # Clean previous builds
    if os.path.exists('dist'):
        print("Cleaning previous build...")
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')

    # Set environment variables to avoid OpenSSL issues
    env = os.environ.copy()
    env['PYTHONOPTIMIZE'] = '1'

    # Check if running in Anaconda environment
    in_conda = os.path.exists(os.path.join(sys.prefix, 'conda-meta'))
    if in_conda:
        print("Detected Anaconda environment. Using alternative build approach...")

        # Create a virtual environment for building
        print("Creating a temporary virtual environment for building...")
        venv_dir = os.path.abspath('.build_venv')
        if os.path.exists(venv_dir):
            shutil.rmtree(venv_dir)

        # Create venv
        subprocess.run([sys.executable, '-m', 'venv', venv_dir])

        # Get the Python executable in the venv
        if sys.platform.startswith('win'):
            venv_python = os.path.join(venv_dir, 'Scripts', 'python.exe')
        else:
            venv_python = os.path.join(venv_dir, 'bin', 'python')

        # Install required packages in the venv
        print("Installing required packages in the virtual environment...")
        subprocess.run([venv_python, '-m', 'pip', 'install', '--upgrade', 'pip'])
        subprocess.run([venv_python, '-m', 'pip', 'install', 'pyinstaller', 'PySide6==6.9.0'])

        # Build command for venv
        cmd = [
            venv_python, '-m', 'PyInstaller',
            '--clean',
            '--noconfirm',
            '--windowed',
            '--name=PalinDrome',
            '--add-data=src/main_window.ui:src',
            '--add-data=src/app/main.py:src/app',
            '--hidden-import=PySide6.QtCore',
            '--hidden-import=PySide6.QtGui',
            '--hidden-import=PySide6.QtWidgets',
            '--hidden-import=src.app.main',
            '--hidden-import=src.main_window',
            # Exclude problematic modules
            '--exclude-module=PySide6.QtNetwork',
            '--exclude-module=PySide6.QtWebEngineCore',
            '--exclude-module=PySide6.QtWebEngine',
            '--exclude-module=PySide6.QtWebEngineWidgets',
            'src/app/main.py'
        ]
    else:
        # Standard build command
        cmd = [
            'pyinstaller',
            '--clean',
            '--noconfirm',
            '--windowed',
            '--name=PalinDrome',
            '--add-data=src/main_window.ui:src',
            '--add-data=src/app/main.py:src/app',
            '--hidden-import=PySide6.QtCore',
            '--hidden-import=PySide6.QtGui',
            '--hidden-import=PySide6.QtWidgets',
            '--hidden-import=src.app.main',
            '--hidden-import=src.main_window',
            # Exclude problematic modules
            '--exclude-module=PySide6.QtNetwork',
            '--exclude-module=PySide6.QtWebEngineCore',
            '--exclude-module=PySide6.QtWebEngine',
            '--exclude-module=PySide6.QtWebEngineWidgets',
            'src/app/main.py'
        ]

    # Adjust command for Windows if needed
    if sys.platform.startswith('win'):
        # Replace all data paths with Windows-style paths
        for i, arg in enumerate(cmd):
            if arg.startswith('--add-data='):
                cmd[i] = arg.replace(':', ';')

    print("Running PyInstaller with command:", ' '.join(cmd))

    # Run PyInstaller
    result = subprocess.run(cmd, env=env)

    if result.returncode == 0:
        print("Build completed successfully!")
        print(f"Executable can be found in {os.path.abspath('dist/PalinDrome')}")

        # Clean up venv if created
        if in_conda and os.path.exists(venv_dir):
            print("Cleaning up temporary virtual environment...")
            shutil.rmtree(venv_dir)
    else:
        print("Build failed with error code:", result.returncode)
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
