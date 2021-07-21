#concatinate
"some" + "text"
str(1) + " is an Integer"

#convert to string
str(some non string data)

#length of string
len("a string")
data = "a string"
data.__len__

#read text from network request response 
response.text
#size of the request response
len(response.content)

#take user input
data = input("Enter What you Want: ")

#find and replace from text string
astring = "this text"
replaced = astring.replace("this", "with that")
#output will be: 
# ........with that text...........

# join two path into one
from os import path
os.path.join(basePath, cznId.replace("/", ""))


#find number of files in a directory
import os
path, dirs, files = next(os.walk("Citizens"))
file_count = len(files)
print(file_count)

#use threading, its something like coroutines in kotlin
def myFunc(arg):
  print(arg)
  
from threading import Thread
Thread(target=myFunc, args=(1, )).start()
Thread(target=myFunc, args=(2, )).start()

#pause or delay working process like this
import time
for x in range(1,5):
  print(x)
  time.sleep(1)   #where 1 is a one second (time is in seconds)
  
  
  
#Make a directory if its does not exists
from os import makedirs
def makeFilePath (dirName):
    if not os.path.isdir(dirName):
        os.mkdir(dirName) #make directory if it doesn't exist
        print("Created Directory " + dirName)

#check if a file exists or not
from pathlib import Path

filePath = "path/to/file"
if Path(filePath).is_file(): 
  print("File Found")
 else: 
  print("File Not Found")
