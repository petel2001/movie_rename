# rename script - will rename movie files to all lower case
import os
def rename_movie():
    file_list = os.listdir(r"/Users/lpeterso/Documents/TEMP/movies")
    saved_path = os.getcwd()
    os.chdir(r"/Users/lpeterso/Documents/TEMP/movies")
    for file_name in file_list:
        os.rename(file_name, file_name.lower())
    os.chdir(saved_path)
    print 'rename complete'

rename_movie()