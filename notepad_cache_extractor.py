import os
import re

def extract_readable_strings(data):
    """
    Extract readable ASCII and UTF-16LE encoded strings from binary data.
    """
    # For ASCII strings: Look for sequences of printable characters
    ascii_strings = re.findall(b"[ -~]{4,}", data)
    
    # For UTF-16LE strings: Look for sequences of characters separated by null bytes
    utf16_strings = re.findall(b"(?:[\x20-\x7E]\x00){4,}", data)

    # Decode found strings
    decoded_ascii_strings = [s.decode("ascii") for s in ascii_strings]
    decoded_utf16_strings = [s.decode("utf-16le") for s in utf16_strings]

    # Combine and return all strings
    return decoded_ascii_strings + decoded_utf16_strings

def process_tabstate_file(filepath):
    """
    Process a TabState file to extract and print readable strings.
    """
    with open(filepath, 'rb') as file:
        data = file.read()

    strings = extract_readable_strings(data)
    if strings:
        print(f"\nExtracted strings from {os.path.basename(filepath)}:")
        for string in strings:
            print(string)
    else:
        print(f"No readable strings found in {os.path.basename(filepath)}.")

def main():
    directory = r"C:\Users\[USERNAME]\AppData\Local\Packages\Microsoft.WindowsNotepad_[RANDOMSTRING]\LocalState\TabState"
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".bin"):
                filepath = os.path.join(root, file)
                process_tabstate_file(filepath)

if __name__ == "__main__":
    main()
