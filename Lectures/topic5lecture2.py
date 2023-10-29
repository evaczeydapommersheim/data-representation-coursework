# Topic 5 Lecture 2 Lab preparation GitHub
# Look at the GitHub API

import requests
import json

# filename = "repo-public.json"
filename1 = "repo-private.json"

# url = 'https://api.github.com/repos/ansdrewbeattycourseware/datarepresentation/contents/'
url = 'https://api.github.com/repos/evaczeydapommersheim/aprivateone'
apikey = "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"

response = requests.get(url, auth = ('token', apikey))
print(response.status_code)
repoJSON = response.json()

with open(filename1, 'w') as fp:
    json.dump(repoJSON, fp, indent = 4)