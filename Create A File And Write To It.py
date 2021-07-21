#create and save data in the file
def writeToFile (fileAddress, data):
    file = open(fileAddress, "w")
    file.write(data.text)
    file.close
    with open("myfileName.text", "a") as myfile:
      myfile.write(data)
    print("File Created !")
    
#the use like this
writeToFile("aLocationToSave", "DataToWriteInFile") 
