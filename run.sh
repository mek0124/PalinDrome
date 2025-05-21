#!/bin/bash

# Convert UI to Python
pyside6-uic src/main_window.ui -o src/main_window.py

# Build the project
python3 build.py

# Run the project
./dist/PalinDrome/PalinDrome