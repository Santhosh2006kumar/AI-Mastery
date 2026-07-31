#auth in requests using python

import requests

r = requests.get("https://echo.free.beeceptor.com/basic-auth/Sandy/1234",auth=('Sandy','12356'))

print(r.status_code)

print(r.text)