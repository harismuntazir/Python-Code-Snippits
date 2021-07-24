import requests

series = input("Enter Series: ")
base = "CZN/01/02/" + series + "/"
sessionID = "688B24896C1DA15474BC493CB2CCFBF2"

#make file name
def makeFileName(idx):
    zeros = ["000000","00000","0000","000","00","0", ""]
    for i in range(1, 8):
        if len(str(idx)) == i:
            return base +  zeros[i-1] + str(idx)
 
#make link
def makeLink (fileName):
    return "https://example.com/profile.php?id=" + fileName  
 
#get data from server
def getData (link):
    payload={}
    headers = {
        'Cookie': 'JSESSIONID=' + sessionID
    }
    return requests.request("GET", link, headers=headers, data=payload)

#find upper limit of the series
def getLimit(upperLimit):
  isClose = 0
  round = 0
  lost = True
  while lost:
    print(upperLimit)
    data = getData(makeLink(makeFileName(upperLimit)))
    if upperLimit < 0:
      return -1
    if len(data.content) > 190000:
      if round == 0:
        upperLimit += 10000
      if round == 1:
        isClose = 1
        upperLimit += 1000
      if round == 2:
        isClose = 2
        upperLimit += 100
      if round == 3:
        isClose = 3
        upperLimit += 10
      if round == 4:
        isClose = 4
        upperLimit += 1
    else:
      if isClose == 0:
        round = 1
        upperLimit -= 5000
      if isClose == 1:
        round = 2
        upperLimit -= 500
      if isClose == 2:
        round = 3
        upperLimit -= 50
      if isClose == 3:
        round = 4
        upperLimit -= 5
      if isClose == 4:
        upperLimit -= 1
        lost = False     
        print ("Upper Limit Found At: " + str(upperLimit))
        return upperLimit
      
#the use like this
print(getLimit(1))
