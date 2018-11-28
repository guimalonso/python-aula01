import requests

#re = requests.get('http:///httpbin.org/ip')
#print(re.json())

headers = {"Content-type": "application/json"}
data = {"nome": "daniel"}

re = requests.post(
    "http://127.0.0.1:5000/",
    data = data
)