import os
import requests

from dotenv import load_dotenv

load_dotenv()


response = requests.get("https://foodish-api.com/api/images/pizza")
print(response)
if response.status_code == 200:
   
    print(response.json())
    print(response.json()["image"])
else:
    print("error", response.status_code)
 