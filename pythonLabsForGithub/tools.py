import pandas as pd
import numpy as np
import os
import glob

def is_file_exist(path):
    """
    the function checks the full path's existence in the current directory and returns a boolean 
    """
    full_path = os.path.join(os.getcwd(),path)
    return os.path.isfile(full_path) 


def check_file(filename):
    """
    if the file in path exists return True, else False
    """
    fullname = os.path.join(os.getcwd(),filename)
    
    if os.path.isfile(fullname):
        return True
    else:
        return False
# we create this function to be resuable 


def read_dataset(path,colnames=None): 
    '''
    the function reads the dataset via a path and retunrs a dataframe 

    '''
    if check_file(path) == True:
        df=pd.read_csv(path, header=colnames)
    else:
        df = None
    return df


def list_files_cur():
    '''
    This function returns the list of the files in the current directory
    '''
    current_directory = os.getcwd()
    result = os.listdir(current_directory)
    return result

def list_file_with_extension_cur_glob(extension):
    '''
    This function returns the list of the files with a given extension in the current directory
    using glob
    '''
    extension = extension.strip()
    if extension.startswith('.'): # Check if there is a . at the begining of the extension
        extension = extension[1:] # if yes, select only the extension fomr the 2nd character
    allowed = ['pdf','csv','data','txt'] # list of allowed extensions
    try:
        if extension not in allowed:
            raise ValueError
        else:
            current_directory = os.getcwd()
            full_path = os.path.join(current_directory, '*.' + extension)
            return glob.glob(f"*.{extension}")
    except:
        print('Extension used is not allowed, please used one of these : ')
        print(str(allowed))