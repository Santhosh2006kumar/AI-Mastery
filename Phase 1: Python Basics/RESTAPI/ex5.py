# post method using requests

import requests

payload = {'username': "santhosh kumar",'password':'ssk@426'}

r = requests.post("https://echo.free.beeceptor.com/post",data=payload)

print(r.status_code)

print(r.text)

# we can convert the output into dictionary using json so that we can easily access the response output

r_dict = r.json()

print(r_dict)

print("Getting Username and Password")

print("\nUSERNAME: ",r_dict.get("parsedBody")['username'])
print("\nPASSWORD: ",r_dict.get("parsedBody")['password'])