# instead of using urllib -> urlopen we use requests to fetch the json data and display the same

import requests
import json

r = requests.get("https://api.github.com/users/hadley/orgs")

print("response status: ",r)
# print(dir(r))

# print(r.text)

data = r.text 
data = json.loads(data)

for data in data:
    print("ID: ",data.get("id"))
    print("URL: ",data.get("url"))
    print("REPOS URL: ",data.get("repos_url"))
    print("EVENT URL: ",data.get("events_url"))
    print("HOOKS URL: ",data.get("hooks_url"))
    print("ISSUES URL: ",data.get("issues_url"))
    print("MEMBERS URL: ",data.get("memebers_url"))
    print("PUBLIC MEMBERS URL: ",data.get("public_members_url"))
    print("AVATAR URL: ",data.get("avatar_url"))
    print("DESCRIPTION: ",data.get("description"))
    print()