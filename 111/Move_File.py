import os , shutil ;

from_dir = "C:/Users/Anaya/Downloads"
to_dir = "C:/Users/Document_Files/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

 name,extension = os.path.splittext(file_name)
