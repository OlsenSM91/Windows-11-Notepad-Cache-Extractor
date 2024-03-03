import os
import re
import glob

def extract_readable_strings(data):
    ascii_strings = re.findall(b"[ -~]{4,}", data)
    utf16_strings = re.findall(b"(?:[\x20-\x7E]\x00){4,}", data)
    decoded_ascii_strings = [s.decode("ascii") for s in ascii_strings]
    decoded_utf16_strings = [s.decode("utf-16le") for s in utf16_strings]
    return decoded_ascii_strings + decoded_utf16_strings

def process_tabstate_file(filepath):
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
    localappdata = os.getenv('LOCALAPPDATA')
    base_dir = os.path.join(localappdata, 'Packages')
    notepad_dirs = [d for d in os.listdir(base_dir) if 'Microsoft.WindowsNotepad_' in d]

    for notepad_dir in notepad_dirs:
        tabstate_dir = os.path.join(base_dir, notepad_dir, 'LocalState', 'TabState')
        for filepath in glob.glob(os.path.join(tabstate_dir, '*.bin')):
            # Skip files ending with .0.bin or .1.bin
            if filepath.endswith('.0.bin') or filepath.endswith('.1.bin'):
                continue
            process_tabstate_file(filepath)

if __name__ == "__main__":
    main()
