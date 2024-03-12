# Output tabstate binary contents with powershell, could be easily included in a Rubber Ducky script
# Written by: Steven Olsen and ChatGPT

function Extract-ReadableStrings {
    param (
        [byte[]]$Data
    )

    # Initialize a list to store extracted strings
    $extractedStrings = New-Object System.Collections.Generic.List[System.String]

    # Convert the byte array to a UTF-16LE string
    $utf16String = [System.Text.Encoding]::Unicode.GetString($Data)

    # Use regex to find sequences of printable characters
    # Adjusting the regex to closely match the Python script's logic
    $matches = [regex]::Matches($utf16String, "([ -~`\r\n]{4,})")
    foreach ($match in $matches) {
        $extractedStrings.Add($match.Value)
    }

    return $extractedStrings
}

function Process-TabStateFile {
    param (
        [string]$FilePath
    )

    # Read the file as a byte array
    $data = [System.IO.File]::ReadAllBytes($FilePath)
    $strings = Extract-ReadableStrings -Data $data

    if ($strings.Count -gt 0) {
        Write-Output "`nExtracted strings from $(Split-Path -Leaf $FilePath):"
        $strings | ForEach-Object { Write-Output $_ }
    } else {
        Write-Output "No readable strings found in $(Split-Path -Leaf $FilePath)."
    }
}

$localAppData = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::LocalApplicationData)
$baseDir = Join-Path -Path $localAppData -ChildPath "Packages"
$notepadDirs = Get-ChildItem -Path $baseDir -Directory | Where-Object { $_.Name -like "Microsoft.WindowsNotepad_*" }

foreach ($notepadDir in $notepadDirs) {
    $tabStateDir = Join-Path -Path $notepadDir.FullName -ChildPath "LocalState\TabState"
    if (Test-Path $tabStateDir) {
        $filePaths = Get-ChildItem -Path $tabStateDir -File | Where-Object { $_.Name -notmatch ".0.bin$|.1.bin$" }
        foreach ($filePath in $filePaths) {
            Process-TabStateFile -FilePath $filePath.FullName
        }
    }
}
