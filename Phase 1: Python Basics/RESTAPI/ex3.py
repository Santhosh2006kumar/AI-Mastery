#status code

# 200's - Success
# 300's - redirects
# 400's - client errors (occured when we don't have permission to view / use that url)
# 500's - server errors (the site get crashed)

#------------------------------------------------------------
# NOTE1:
# In Python's requests library, the timeout parameter tells Python how long to wait for a server to respond before giving up.

# By default, if you don't pass timeout, requests will wait indefinitely for a response. 
# #If a server freezes or hangs, your program will get stuck forever.
# syntax:-

# r = requests.get("url",timeout=n) n = number for example 3
# r = requests.get("https://api.github.com/users/hadley/orgs",timeout=3)

# ----------------------------------------------------------------

import requests

r = requests.get("https://api.github.com/users/hadley/orgs")

print(r.status_code) # prints the response status of that request


print(r.ok)  # returns true if the status_code is <400
             # returns false if the status_code is >400 i.e., if we get client side or server side errors

print(r.headers) # getting header details