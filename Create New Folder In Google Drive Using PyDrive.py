import pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
 
# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()

drive = GoogleDrive(gauth)
# To create a new folder
folder_name = input("Name the Folder : ")
folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
folder.Upload()
print(folder.metadata['id'])
