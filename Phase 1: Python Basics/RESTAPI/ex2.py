# getting image from url and store it as a image file in your local machine using requests

import requests

r = requests.get("https://newsarenaindia.com/_next/image?url=https%3A%2F%2Fimages.newsarenaindia.com%2Fvijaynai-1jpg_1782108575292.jpg&w=1920&q=75")

print("resposne status:",r)

print("Image Bytes: ")

print(r.content)

# convert that image bytes into a image (vijay.png)

with open('vijay.png','wb') as v:
    v.write(r.content)
    print("Image Saved Successfully !")