# GET request with parameters using requests in python

import requests

payload = {'page':3,'count':25}
r = requests.get("https://echo.free.beeceptor.com/get",params=payload)

print("Response Status: ")
print(r.status_code)
if(r.status_code==200):
    print("Success")

print("\nComplete URL including parameters: \n")
print(r.url)

print("\nSome Text content: \n")
print(r.text)


