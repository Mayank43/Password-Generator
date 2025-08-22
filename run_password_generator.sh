#!/bin/bash

echo "========================================"
echo "   Password Generator - by Mayank43"
echo "========================================"
echo ""
echo "Starting Password Generator..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
if ! python3 -c "import pyperclip" &> /dev/null; then
    echo "Installing required packages..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install requirements"
        exit 1
    fi
fi

# Run the application
echo "Starting application..."
python3 password_generator.py

echo ""
echo "Application closed."
