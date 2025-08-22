# Password Generator - by Mayank43

A powerful and user-friendly password generator application built with Python and Tkinter. Generate secure, customizable passwords with just a few clicks!

## Features

- **Random Password Generation**: Generate cryptographically secure random passwords
- **Length Customization**: Adjust password length from 4 to 50 characters
- **Character Type Selection**: Choose which character types to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*)
- **Exclusion Options**: Exclude similar or ambiguous characters for better readability
- **One-Click Copy**: Copy generated passwords to clipboard instantly
- **Password History**: View and manage previously generated passwords
- **Persistent Storage**: Passwords are saved locally for future reference
- **Modern UI**: Beautiful, intuitive interface with dark theme

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mayank43/Password-Generator.git
   cd Password-Generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python password_generator.py
   ```

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pyperclip

## How to Use

1. **Launch the application** by running `python password_generator.py`
2. **Adjust settings**:
   - Set desired password length using the slider
   - Check/uncheck character types you want to include
   - Optionally exclude similar or ambiguous characters
3. **Generate password** by clicking the "Generate Password" button
4. **Copy to clipboard** using the "Copy to Clipboard" button
5. **View history** to see previously generated passwords

## Customization Options

### Character Types
- **Uppercase Letters**: A-Z (26 characters)
- **Lowercase Letters**: a-z (26 characters)
- **Numbers**: 0-9 (10 characters)
- **Symbols**: !@#$%^&*()_+-=[]{}|;:,.<>? (20+ characters)

### Exclusion Options
- **Similar Characters**: Excludes l, 1, I, O, 0 to avoid confusion
- **Ambiguous Characters**: Excludes {}, [], |, \, /, ", ' for better compatibility

## Screenshots

The application features a modern dark theme with:
- Clean, intuitive interface
- Real-time length display
- Status bar with feedback
- Organized settings panel
- Professional color scheme

## Security Features

- **Cryptographically Secure**: Uses Python's `random` module for secure generation
- **No Network Access**: All operations are performed locally
- **Local Storage**: Password history is stored locally in JSON format
- **No Data Collection**: No personal data is collected or transmitted

## Project Structure

```
Password-Generator/
├── password_generator.py    # Main application file
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── run_password_generator.bat  # Windows launcher
├── run_password_generator.sh   # Linux/Mac launcher
└── password_history.json   # Password history (created after first use)
```

## UI Components

- **Main Window**: 500x900 pixels with dark theme
- **Password Display**: Large, readable font for generated passwords
- **Settings Panel**: Organized checkboxes and sliders
- **Action Buttons**: Color-coded buttons for different functions
- **History Window**: Separate window with table view
- **Status Bar**: Real-time feedback and information

## Version History

- **v1.0**: Initial release with core functionality
  - Password generation with customization
  - Clipboard integration
  - Password history
  - Modern UI design

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Mayank43**
- GitHub: [@Mayank43](https://github.com/Mayank43)

## Acknowledgments

- Built with Python and Tkinter
- Modern UI design principles
- Clean and efficient code structure

## Support

If you encounter any issues or have suggestions, please:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Include your Python version and operating system

---

**Star this repository if you find it useful!**
