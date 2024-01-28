from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import os
import sys
import yaml
import base64

def read_yaml_file(file_path:str)->dict:
    """
    Description: This function reads a yaml file and returns a dictionary of items.

    Return: Dictionary

    """
    try:
        with open(file_path,'rb') as yaml_file:
            logging.info(f"Yaml file loaded from path {file_path} sucessfully")
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise SignException(e,sys)
    
def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    """
    Description: This fuction checks the path to write a yaml file if exist remove the path,
                 removes the path and write a new yaml file.
    Return: None
                 
    """
    try:
        if replace:
            if os.path.exists(file_path):
                logging.info("older file removed")
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,'w') as file:
            yaml.dump(content,file)
            logging.info(f"Successfully written on file path {file_path}")

    except Exception as e:
        raise SignException(e,sys)
    
def decodeImage(imgstring,filename):
    """
    Description: This function decode an image and write it in binary format.

    Return: None

    """
    try:
        imgdata= base64.b64decode(imgstring)
        with open("./Data/" + filename , 'wb') as f:
            f.write(imgdata)
            f.close()

    except Exception as e:
        raise SignException(e,sys)
    

def encodeImageIntoBase64(croppedImagePath):
    """
    Description: This function reads the binary data from the file, then encodes it into base64.

    Return: base64-encoded data

    """
    try:
        with open(croppedImagePath, "rb") as f:

            return base64.b64encode(f.read())
        
    except Exception as e:
        raise SignException(e,sys)