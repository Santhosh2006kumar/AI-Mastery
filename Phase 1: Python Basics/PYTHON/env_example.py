import os
from dotenv import load_dotenv

load_dotenv()

name=os.getenv("NAME")
print(name)

email=os.getenv("EMAIL")
print(email)

topic=os.getenv("TOPIC")
print(topic)
