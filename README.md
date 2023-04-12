This script uses the `tkinter` and `PySimpleGUI` libraries to create a graphical user interface for selecting source and destination paths, as well as displaying progress bars.

# File Synchronization Script

This Python script synchronizes files and directories from a source folder to a destination folder. It will copy files and directories that do not exist in the destination folder or if the file sizes differ. The script also provides a graphical user interface (GUI) to browse and select the source and destination folders.

## Requirements

- Python 3.6 or newer
- PySimpleGUI
- tkinter

## Installation

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python file_sync.py
   ```
2. Follow the prompts in the GUI to select the source and destination folders.
3. The script will synchronize the files and display progress bars indicating the progress of individual file transfers and the overall synchronization process.

## Notes

- The script does not delete files in the destination folder that do not exist in the source folder.
- The script overwrites files in the destination folder if their sizes differ from the corresponding files in the source folder.
```

And here's a `requirements.txt` for the code:

```
PySimpleGUI==4.53.0
```

Note that `tkinter` is part of the Python standard library, so it doesn't need to be included in the `requirements.txt` file. However, it may need to be installed separately on some Linux distributions.



# transfer-helper
A file transfer tool that copies the files and directories from a source path to a destination path.  If a file in the destination path already exists, the script checks the size of both files and updates the destination file if the sizes are different. It also provides a progress bar to track the progress of the file transfer.

Here's a brief overview of the script's structure:

1. Import necessary libraries.
2. Define helper functions for file and directory management, such as:
   - is_path()
   - is_file()
   - getDir()
   - browse_files()
   - change_glob()
   - list_directory()
   - path_join()
   - get_paths()
   - progBar()
   - trunc()
   - update_prog()
   - mkGb()
   - mkGbTrunk()
   - mkGbTrunFroPathTot()
   - lsDir()
   - pathJoin()
   - progress_bar_callback()
   - copy_file_or_directory()
   - get_size()
   - get_total_size()
   - lsDir()

3. Define the progress bar window using the `progBar()` function.
4. Get the source and destination paths using the `get_paths()` function.
5. Iterate through the files and directories in the source path, and perform the following actions:
   - If the destination directory doesn't exist, create it.
   - If a file doesn't exist in the destination directory, copy it from the source directory.
   - If a file with the same name already exists, compare their sizes and update the destination file if needed.
   
6. Update the progress bars accordingly.
