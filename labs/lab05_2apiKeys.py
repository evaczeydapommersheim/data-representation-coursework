# By Eva Czeyda-Pommersheim

import requests
import urllib.parse
from config1 import config as cfg

targetUrl = "https://en.wikipedia.org"
apiKey = cfg["htmltopdfkey"]
apiUrl = "https://api.html2pdf.app/v1/generate"

params = {'url': targetUrl, 'apiKey' : apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiUrl +"?"+ parsedparams

response = requests.get(requestUrl)
print(response.status_code)

result = response.content
with open("wikipedia.pdf", "wb") as handler:
    handler.write(result)

