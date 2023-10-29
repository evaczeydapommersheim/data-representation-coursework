# Lab05_03 as part of Topic05
import requests
from github import Github
from config2 import config as cfg

apikey = cfg["apiKey"]
g = Github(apikey)

#for repo in g.get_user().get_repos():
    #print(repo.name)

repo = g.get_repo("evaczeydapommersheim/aprivateone")
# print(repo.clone_url)
# repo.create_file("test.txt", "test", "test")
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

# print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

newContents = contentOfFile + " more stuff \n"
#print(newContents)

gitHubResponse = repo.update_file(fileInfo.path, "even more stuff", newContents, fileInfo.sha)
print(gitHubResponse)