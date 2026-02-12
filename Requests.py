import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
response_json = response.json()

print(response_json["url"]) # <Response [200]>
