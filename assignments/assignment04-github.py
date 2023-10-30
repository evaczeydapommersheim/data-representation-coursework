# Program is to read a file from a repository
# program is to replace all instances of the text "Andrew" with my name
# Program to commit changes and push file back to the repository

#By: Eva Czeyda-Pommersheim

# Importing the necessary modules:
import requests
from github import Github

# using a config file which includes API Key to a private repositroty in GitHub:
from config2 import config as cfg

# application of API Key to access repository on GitHub
apikey = cfg["apiKey"]
g = Github(apikey)

# assigning text to file that is to be created in GitHub Repository:
content = "This file is to include the word Andrew multiple time. Andrew gave is an assigment, where Andrew requires us to write code to replace the name Andrew with our own name."
# accessing private repository
repo = g.get_repo("evaczeydapommersheim/aprivateone")

# Created a file with the name Andrew in it in Privat GitHub repository
# (later commented it out):
#repo.create_file("assignment04.txt", "creating file", content) 

# Accessing the content of the created file
fileInfo = repo.get_contents("assignment04.txt")

#Downloading file and printing its content (print command commented once it worked)
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

# Replacing the word Andrew with my name and print
# print command commented out once it worked
newContent = contentOfFile.replace("Andrew", "Eva")
#print(newContent)

# Update the file on GitHub by adding the path, message and the updated content
# Pushing it back to GitHub repository
gitHubResponse = repo.update_file(fileInfo.path, "replacement complete", newContent, fileInfo.sha)
print(gitHubResponse)
    

