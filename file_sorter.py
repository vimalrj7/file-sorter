import os
import shutil

def sort_files(extension):
    files_list = (file for file in os.listdir(os.getcwd()) if file.endswith('.' + extension))
    os.makedirs(extension + ' files')

    for file in files_list:
        source = os.path.abspath(file)
        dest = os.getcwd() + '\\' + extension + ' files\\' + file
        shutil.move(source, dest)
        
    print("Moved files into " + extension + " folder!")
    
def get_extensions():
    ext_list = []
    for file in os.listdir(os.getcwd()):
        ext = file.split(".")[-1]
        if ext not in ext_list:
            ext_list.append(ext)
    print("Here are the different file formats in this folder: ")
    print(", ".join(ext_list))
    
def main():
    get_extensions()
    formats = input("Type down the file formats you want to sort, separated by a comma (eg: jpeg, png, raw)").split(", ")
    for format in formats:
        sort_files(format)
    
main()