from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
 
# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default() 

def toDrive(name, contents, isFile = False):
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': name}) 

    if isFile:
      file.SetContentFile(contents)
    else:
      file.SetContentString(contents) 
    
    file.Upload()
    print("File Uploaded To Google Drive Successully")
    
    
#now to use this 
#to save some raw text, follow like this
toDrive("file.txt", "some text data as content")
#if you want to save a file in its whole, do this
toDrive(fileName, fileLocation, True)     #by using true we say its a file 


#for more features follow this
#https://pythonhosted.org/PyDrive/

#above method will ask for a code from your google drive api with every new session created
#to save this shit code for a few more moments or days, follow along like this

#in the woking directory create a file named  # settings.yaml and add the below contents

client_config_backend: settings
client_config:
  client_id: your_client_id
  client_secret: your_client_secret

save_credentials: True
save_credentials_backend: file
save_credentials_file: credentials.json

get_refresh_token: True

oauth_scope:
  - https://www.googleapis.com/auth/drive.file
  - https://www.googleapis.com/auth/drive.install


#then in the worker file follow like this
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

#authenticate once every new session
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

def toDrive(contents, name):
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': name}) 
    file.SetContentString(contents) # Set content of the file from given string.
    file.Upload()
    print("File Uploaded To Google Drive Successully")

toDrive("hey this is haris testing pydrive", "text.txt")
