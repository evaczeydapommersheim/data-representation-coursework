import requests
import json
from config2 import config as cfg

filename = "repo-private.json"

url = 'https://api.github.com/repos/evaczeydapommersheim/aprivateone'
apiKey = cfg["apiKey"]

response = requests.get(url, auth = ('token', apiKey))
print(response.status_code)
repoJSON = response.json()

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent = 4)