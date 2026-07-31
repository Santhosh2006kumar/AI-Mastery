import json
from urllib.request import urlopen

with urlopen("https://api.github.com/users/hadley/orgs") as f:
    data = f.read()

# print(data)

data = json.loads(data)

for data in data:
    print(data.get("id"))
    print(data)
