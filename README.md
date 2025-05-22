<label id="top"></label>

<div align="center">
  <img src="./app-icon.jpeg" height="120" width="120" />
  <h1>PalinDrome</h1>
</div>

A simple desktop application for checking if your word or phrase is the same spelled forwards as it is backwards.

> NOTE: If you want the application packaged down into a windows executable, then you will need to package it yourself. 
>       I have tried and tried until I am just done with trying to build a .exe for windows while on a linux system.

## How To Use

1. Clone the Repo

    ```
    git clone https://github.com/mek0124/PalinDrome.git
    ```

2. To run the app

    ```
    bash run.sh
    ```

    - This script is setup to convert all .ui files found in src/ to .py files before packaging.

    - This script is setup to automatically check for the `dist` and `build` folders for the project. If they do not exist, it will build the application down and launch it for you.

# Standalone Installer

## Download Pre-built Versions

- Windows: [PalinDrome.exe](https://example.com/PalinDrome.exe) (Just double-click to run)
- macOS: [PalinDrome.app.zip](https://example.com/PalinDrome-macOS.zip) (Unzip and drag to Applications)
- Linux: [PalinDrome.sh](https://example.com/PalinDrome-Linux.sh) (Run `chmod +x` then execute)

## For Developers

To build from source:
```bash
git clone https://github.com/yourusername/PalinDrome.git
cd PalinDrome
./package.sh  # Creates all platform packages
```

### 5. New `.github/workflows/release.yml` for auto-building:
```yaml
name: Release

on: [push]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, macos-latest, ubuntu-latest]
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: pip install pyinstaller PySide6
        
    - name: Build
      run: python build.py
      
    - name: Package
      run: |
        if [[ "$RUNNER_OS" == "Windows" ]]; then
          7z a PalinDrome-Windows.zip dist/PalinDrome.exe
        elif [[ "$RUNNER_OS" == "macOS" ]]; then
          zip -r PalinDrome-macOS.zip dist/PalinDrome.app
        else
          tar -czvf PalinDrome-Linux.tar.gz dist/PalinDrome
        fi
        
    - name: Upload
      uses: actions/upload-artifact@v2
      with:
        name: PalinDrome-${{ runner.os }}
        path: PalinDrome-*
```

## Updating

This application comes with a method to check the current version (in the app/version.txt) versus the latest release on GitHub. If these versions <b><u>do not match</u></b> the application will <b><u>prompt for an update</u></b>. If you <b><u>do not want to update</u></b> then click **No** on the popup dialog. Keep in mind, you will be <b><u>prompted to update</u></b> on each launch. This is because (but not limited to) any updates that may come along, changes in client-side frameworks, api's libraries, etc.

## Features

- Checks if a word, or phrase, is the same forwards and backwards
- Option to ignore CaseSensitivity with spelling
- Ignores all punctuation.
- Update feature to assist in maintaining the code base

## Issues

If at any point you come into any issues, please create [a new issue](https://github.com/mek0124/PalinDrome/issues) and I will respond as soon as I can. If you do not get a response from me, be sure to check the repo for updates. 