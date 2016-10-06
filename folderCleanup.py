
import os
from shutil import copyfile

# Import dictionary of files to keep
from keep import keep

# Current Directory
dir_path = os.path.dirname(os.path.realpath(__file__))

stuff_to_clean = os.listdir(r"PATH OF stuff_to_clean")
cleaned_stuff = r"PATH of cleaned_stuff"

# Function that reads stuff_to_clean directory and stores values into a dictionary called files.  Assumes that first 8 are the primary key of the file_name
def readFolder():
	files = {}
	for stuff in stuff_to_clean:
		files[stuff[:8]] = stuff
	return files

# Function that selects files from stuff_to_clean using the dictionary keep
def moveFiles():
	for k in keep:
		stuff_to_keep = readFolder().get(k)
		stk_path = dir_path + '\\stuff_to_clean\\' + stuff_to_clean
		new_path = dir_path + '\\cleaned_stuff\\' + stuff_to_clean
		try:
			copyfile(stk_path, new_path)
			print('Copying... '+str(stuff_to_clean))
		except Exception as e:
			print(str(e))

moveFiles()
