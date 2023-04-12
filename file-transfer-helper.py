import os
import shutil
import time
from tkinter import filedialog, Tk
import PySimpleGUI as sg
from tkinter.filedialog import askdirectory
def is_path(x):
  return os.path.exists(x)
def is_file(x):
  return os.path.isfile(x)
def getDir():
  return filedialog.askdirectory()
def browse_files(text,start):
      dirPath = getDir()
      filename = filedialog.askopenfilename(initialdir = dirPath,title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
      if filename in [(),'',None]:
        return dirPath,''
      return dirPath,filename.split('/')[-1]
def change_glob(x,y):
      globals()[x] = y
      return y
def list_directory(x):
  if is_file(x):
      return [x]
  elif is_path(x):
      return os.listdir(x)
  return [x]
def path_join(x, y):
  return os.path.join(x, y)
def get_paths():
  files = browse_files('What is the initial folder or document?', os.getcwd())
  change_glob('og_ls',list_directory(path_join(files[0],files[1]))),change_glob('og_Path',files[0])
  files = browse_files('Input the destination path', os.getcwd())
  change_glob('back_ls',list_directory(path_join(files[0],files[1]))),change_glob('back_Path',files[0])
def progBar(key):
      layout = [
         [sg.ProgressBar(0, orientation='h', expand_x=True, size=(20, 20),  key=key)],
         [sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True)]
      ]
      window = sg.Window('Progress Bar', layout)
      while True:
         event, values = window.read()
         break
         window[key].update(max=100)
         window.close()
         if eye == 0:
                 window.close()
         if event == 'Cancel':
            window[key].update(max=100)
         if event == sg.WIN_CLOSED or event == 'Exit':
            break
      return window

def trunc(a,x):
  temp = str(a)
  for i in range(len(temp)):
      if temp[i] == '.':
          try:
              return float(temp[:i+x+1])
          except:
              return float(temp)      
  return float(temp)
def update_prog(win,js):
      win[js['keys']].update(sg.one_line_progress_meter(js['title'], js['curr']+1,js['max'], js['type']+' : '+js['name'],js['action']))
def mkGb(k):
      return float(float(k)*(10**9))
def mkGbTrunk(k):
      return trunc(mkGb(k),5)
def mkGbTrunFroPathTot(k):
      return trunc(mkGb(s.path.getsize(k),5))
def lsDir(x):
      if isFile(x):
              return [x.split('/')[-1]]
      elif isPath(x):
              return os.listdir(x)
      return [x.split('/')[-1]]
def pathJoin(x,y):
  return os.path.join(x,y)
# Define a function to update the progress bar
def progress_bar_callback(n, block_size, total_size):
  PySimpleGUI.ProgressBar(total_size, 'horizontal',n*block_size, 'green')
def copy_file_or_directory(src_path, dst_path):
  if os.path.isfile(src_path):
      file_size = os.path.getsize(src_path)
      # Open the source and destination files
      with open(src_path, 'rb') as src_file, open(dst_path, 'wb') as dst_file:
          # Copy the contents of the source file to the destination file in chunks of 64KB
          while True:
              buf = src_file.read(64 * 1024)
              if not buf:
                  break
              dst_file.write(buf)

              # Update the progress bar with the number of bytes written so far
              
              updateProg(window,{'title':'transfers','keys':'-PBAR-','curr':mkGbTrunFroPathTot(dst_path),'max':mkGbTrunFroPathTot(file_size),'type':'file','name':dst_path.split('/')[-1],'action':'copying'})
  elif os.path.isdir(src_path):
      shutil.copytree(src_path, dst_path)
def get_size(path):
  if os.path.isfile(path):
      return os.path.getsize(path)
  total_size = 0
  for dirpath, dirnames, filenames in os.walk(path):
      for file in filenames:
          fp = os.path.join(dirpath, file)
          try:
                  total_size += os.path.getsize(fp)
          except:
                  total_size += 0
  return total_size
def get_total_size(folder_path):
  total_size = 0
  if os.path.exists(folder_path) and os.path.isdir(folder_path):
      for item in os.listdir(folder_path):
          item_path = os.path.join(folder_path, item)
          total_size += get_size(item_path)
  return total_size
def lsDir(x):
      isFile(x)
      return os.listdir(x)
# Copy the file or directory from the source to the destination
change_glob('window',progBar('-PBAR-'))
change_glob('window2',progBar('-PBAR2-'))
get_paths()
for k in range(0, len(og_ls)):
  src_path = path_join(og_Path, og_ls[k])
  dst_path = path_join(back_Path, og_ls[k])
  # Get the source and destination paths from the command line arguments
  # Define a function to copy a file or directory from the source to the destination
  # Check if the source path exists and is a file or directory
  if not os.path.exists(src_path):
    print(f"Error: {src_path} does not exist")
  # Check if the destination directory exists and is writable
  if not os.path.isdir(dst_path):
    print(f"Error: {dst_path} is not a directory")
  if not os.access(dst_path, os.W_OK):
    print(f"Error: {dst_path} is not writable")
  # Recursively compare the contents of the source and destination directories, and update any files or directories in the destination directory that are smaller than their counterparts in the source directory
  for root, dirs, files in os.walk(src_path):
    rel_root = os.path.relpath(root, src_path)
    dst_root = os.path.join(dst_path, rel_root)
    # Replace '/./' with '/' in the destination path
    for d in dirs:
        src_dir = os.path.join(root, d)
        dst_dir = os.path.join(dst_root, d)
        dst_dir = dst_dir.replace('/./', '/')
        src_dir = src_dir.replace('/./', '/')
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
            print(f"Created directory {dst_dir}")
    for f in files:
        src_file = os.path.join(root, f)
        dst_file = os.path.join(dst_root, f)
        dst_file = dst_file.replace('/./', '/')
        src_file = src_file.replace('/./', '/')
        if not os.path.isfile(dst_file):
            copy_file_or_directory(src_file, dst_file)
            print(f"Copied file {dst_file}")
        else:
            src_file_size = os.path.getsize(src_file)
            dst_file_size = os.path.getsize(dst_file)

            if src_file_size != dst_file_size:
                os.remove(dst_file)
                print(f"Deleted file {dst_file}")
                copy_file_or_directory(src_file, dst_file)
                print(f"Copied file {dst_file}")
    update_prog(window2, {'title': 'Total Progress', 'keys': '-PBAR2-', 'curr': k, 'max': len(og_ls), 'type': 'Total', 'name': 'Block', 'action': 'scanning'}) 
