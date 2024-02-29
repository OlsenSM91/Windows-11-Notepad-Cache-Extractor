import os
import re
import sys

def find_bin_files(directory):
    """
    Find all .bin files in the given directory.

    Parameters:
    directory (str): The directory to search for .bin files.

    Returns:
    list: A list of paths to .bin files found within the directory.
    """
    bin_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".bin"):
                bin_files.append(os.path.join(root, file))
    return bin_files

def extract_strings_from_file(filename):
    """
    Extract readable strings from a binary file.

    Parameters:
    filename (str): Path to the binary file from which to extract strings.

    Returns:
    list: A list of decoded strings extracted from the binary file.
    """
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            # Regular expression to match sequences of printable characters
            strings = re.findall(b'[ -~]{4,}', content)
            return [s.decode('utf-8') for s in strings]
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

def main():
    """
    Main function to find Notepad cache directories, search for .bin files,
    extract printable strings, and save them to text files.
    """
    try:
        base_dir = os.getenv('LOCALAPPDATA') + r'\Packages'
        cache_dirs = [d for d in os.listdir(base_dir) if 'Microsoft.WindowsNotepad_' in d]

        if not cache_dirs:
            print("No Notepad cache directory found.")
            return

        for cache_dir_suffix in cache_dirs:
            full_cache_dir = os.path.join(base_dir, cache_dir_suffix, 'LocalState', 'TabState')
            bin_files = find_bin_files(full_cache_dir)
            if not bin_files:
                print(f"No .bin files found in {full_cache_dir}")
                continue

            for bin_file in bin_files:
                print(f"Extracting strings from: {bin_file}")
                strings = extract_strings_from_file(bin_file)
                if strings:
                    output_filename = bin_file + ".txt"
                    with open(output_filename, 'w', encoding='utf-8') as output_file:
                        output_file.write("\n".join(strings))
                    print(f"Extracted strings saved to: {output_filename}")
                else:
                    print(f"No readable strings found in {bin_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
