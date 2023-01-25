
import zipfile
import os

def unzip(filename):

    # Specify the directory to extract the contents to
    extract_to = 'static\\files\\extracted'

    # Open the zip file
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        # Create the specified directory if it doesn't exist
        os.makedirs(extract_to, exist_ok=True)
        # Extract the contents to the specified directory
        zip_ref.extractall(extract_to)
