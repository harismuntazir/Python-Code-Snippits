import os
import zipfile
    
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))
      

#the use like this  
zipfileName = "MyName.zip"
folderNameToZip = "MyFolder"

zipf = zipfile.ZipFile(zipfileName, 'w', zipfile.ZIP_DEFLATED)
zipdir(folderNameToZip, zipf)
zipf.close()


#now to extract zip file do this
import zipfile
with zipfile.ZipFile('path-to-zip-file', 'r') as zip_ref:
    zip_ref.extractall('location-to-extract')
