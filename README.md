# Windows 11 Notepad Cache Extractor

## Overview
This Python script is designed to extract and export cached data from the Windows 11 Notepad application. The Notepad app in Windows 11 introduces an auto-save feature that retains unsaved documents between sessions by storing them in a binary cache file. This script navigates to the Notepad cache directory, reads the binary cache files, extracts printable strings, and exports them to text files. It's an invaluable tool for recovering unsaved notes or inspecting cached Notepad content.

## Features
- **Automated Discovery**: Dynamically finds the Notepad cache directory, accommodating various directory suffixes used by Windows.
- **String Extraction**: Extracts readable strings from binary cache files, mimicking the functionality of tools like Sysinternals Strings.
- **Error Handling**: Implements robust error handling to gracefully manage access issues, file reading errors, and other potential exceptions.
- **Simple Usage**: Designed with simplicity in mind, requiring only Python to run without the need for additional libraries.

## Requirements
- Python 3.x
- Windows 11 with the Notepad app used at least once (for cache generation)

## Usage
1. **Clone or Download the Script**
   - Clone this repository or simply download the script file to your local machine.

2. **Run the Script**
   - Open a command prompt or PowerShell window.
   - Navigate to the directory containing the script.
   - Execute the script by running:
     ```
     python notepad_cache_extractor.py
     ```
   - Ensure you have the necessary permissions to access the Notepad cache directory. Running the script as an administrator might be required.

3. **Review Extracted Content**
   - The script will create `.txt` files in the same directory as the original cache files. These text files contain the extracted printable strings.

## How It Works
The script first identifies all directories matching the pattern `Microsoft.WindowsNotepad_` within the `%LOCALAPPDATA%\Packages` directory to locate the Notepad cache. It then searches these directories for `.bin` files, reads their content, and uses regular expressions to extract sequences of printable characters. The extracted strings are saved to new text files, providing easy access to the cached Notepad data.

## Limitations
- The script extracts printable strings and may not perfectly reconstruct the original Notepad content if the cache includes non-printable characters or complex formatting.
- It is designed specifically for Windows 11 Notepad's caching mechanism and might not be applicable to other applications or previous Windows versions.

## License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest enhancements.
