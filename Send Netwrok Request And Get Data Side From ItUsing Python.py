import requests

#get data from server
def getData (link):
    payload={}
    headers = {
        'Cookie': 'JSESSIONID=' + sessionID
    }
    return requests.request("GET", link, headers=headers, data=payload)
  
data = getData("https://www.google.com/")
print(len(data.content)) #this will print the request response size
