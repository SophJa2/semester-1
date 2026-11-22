
import httpx
import panda as pd

base_url = "https://dummyjson.com/"

content = "products/search?phone"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data
df = pd.DataFrame(content)


print(df)

#for recipe in range(len(content)-1):
 #   print(content['recipes'][recipe]['difficulty'])
