# Palindrome Checker

A simple desktop application to check if a word is a palindrome (reads the same forwards and backwards).

## Features

- Simple and intuitive user interface
- Instantly checks if a word is a palindrome
- Shows the original word and its reversed version
- Visual indication of the result (green for palindromes, red for non-palindromes)

## Requirements

- Python 3.8 or higher
- PySide6 6.9.0

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application directly with Python:

```bash
python src/app/main.py
```

## Building a Standalone Executable

### Using the build script (recommended)

The build script handles all the necessary configuration to avoid common issues with PyInstaller:

```bash
python build.py
```

The executable will be created in the `dist/PalindromeChecker` directory.

You can run the application using the provided shell script:

```bash
./run_palindrome_checker.sh
```

### Manual build with PyInstaller

If you prefer to use PyInstaller directly:

```bash
pyinstaller --clean --windowed --name=PalindromeChecker --add-data="src/main_window.ui:src" src/app/main.py
```

Note: On Windows, use `;` instead of `:` in the --add-data parameter.

## Troubleshooting

### OpenSSL/Kerberos Issues

If you encounter errors related to OpenSSL or Kerberos when building with PyInstaller, use the provided build script which creates a temporary virtual environment to avoid these issues.

The error:
```
ImportError: /lib/x86_64-linux-gnu/libgssapi_krb5.so.2: undefined symbol: k5_buf_cstring, version krb5support_0_MIT
```

This is resolved by using a clean virtual environment for building, which avoids conflicts with system libraries.

### Anaconda Environment Issues

If you're using Anaconda and encounter the error:
```
ERROR: The 'pathlib' package is an obsolete backport of a standard library package and is incompatible with PyInstaller.
```

The build script automatically detects Anaconda environments and uses a temporary virtual environment to avoid these issues.

### Missing UI File

If you get an error about missing UI file, make sure the UI file is properly included in the build. The build script handles this automatically.

## License

MIT