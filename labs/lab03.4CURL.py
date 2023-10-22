# 2023-24 ATU Data Prepresentation Topic03 Data Transfer
# CURL practice
# By: Eva Czeyda-Pommersheim

import requests

url = 'http://www.githup.com'

response = requests.get(url)
print(response.status_code)


