# Windows 11 Notepad Cache Extractor

## Overview
This Python script is designed to extract and export cached data from the Windows 11 Notepad application. The Notepad app in Windows 11 introduces an auto-save feature that retains unsaved documents between sessions by storing them in a binary cache file. This script automatically discovers the Notepad cache directory, reads the binary cache files, extracts printable strings, including those encoded in UTF-16LE, and prints them to the console. It's an invaluable tool for recovering unsaved notes or inspecting cached Notepad content directly from the command line.

## Features
- **Automated Discovery**: Dynamically finds the Notepad cache directory, accommodating various directory suffixes used by Windows, and handles directory paths with wildcard patterns.
- **Enhanced String Extraction**: Extracts readable ASCII and UTF-16LE encoded strings from binary cache files, improving upon the functionality of tools like Sysinternals Strings by specifically targeting the encoding used by Notepad's cache.
- **Selective Processing**: Ignores cache files known not to contain readable strings (e.g., files ending in `.0.bin` or `.1.bin`), enhancing script efficiency.
- **Robust Error Handling**: Implements robust error handling to gracefully manage access issues, file reading errors, and other potential exceptions.
- **Cross-System Compatibility**: Designed to run on any system with Python, automatically adapting to the user's `%LOCALAPPDATA%` directory without hardcoding paths.

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
   - The script automatically adapts to the system's directory structure; no additional configuration is needed.

3. **Review Output**
   - The script prints extracted strings directly to the console. This immediate output makes it easy to inspect the cached Notepad data without the need for additional file management.

## How It Works
The script navigates to the `%LOCALAPPDATA%\Packages` directory and dynamically identifies all `Microsoft.WindowsNotepad_` directories to locate the Notepad cache. It processes `.bin` files within these directories, excluding those ending in `.0.bin` or `.1.bin`, to extract readable ASCII and UTF-16LE strings. The output is directly printed to the console, providing a straightforward way to access cached Notepad data.

## Limitations
- The script focuses on extracting printable strings and might not reconstruct the original Notepad content if the cache includes non-printable characters or complex formatting.
- Designed specifically for Windows 11 Notepad's caching mechanism; might not be applicable to other applications or previous Windows versions.

## License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest enhancements.
