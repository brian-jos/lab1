import requests
print(requests.__version__) # https://stackoverflow.com/a/20180564

r = requests.get("http://google.com") # https://pypi.org/project/requests/

r2 = requests.get("https://raw.githubusercontent.com/brian-jos/lab1/master/main.py")
print(r2.text)
