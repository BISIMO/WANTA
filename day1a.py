import os
import requests
from dotenv import load_dotenv
load_dotenv()
url = "https://api.restcountries.com/countries/v5/names.common/ghana"
api_key = os.getenv("API_KEY")

response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

print("Status code:", response.status_code)
print("Data received:", response.json())
# test comment