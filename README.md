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

This script uses the `tkinter` and `PySimpleGUI` libraries to create a graphical user interface for selecting source and destination paths, as well as displaying progress bars.
