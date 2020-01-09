import requests

print(requests.__version__)

google = requests.get("http://www.google.com")
print(google)

var = requests.get("https://raw.githubusercontent.com/returnturn/cmput404lab1/master/1.py")

print(var.content)