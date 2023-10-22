# 2023-24 ATU Data Prepresentation Topic04
# This file is to complete Lab04.1 as part of topic reading API-s in the wild.
# By: Eva Czeyda-Pommersheim

import requests

#lab04.1.1
url = "http://google.com"
response = requests.get(url)

# print(response.text)

#lab04.1.2
# Write the code to get the books from http://andrewbeatty1.pythonanywhere.com/books

URL = "http://andrewbeatty1.pythonanywhere.com/books"
# response = requests.get(URL)

# print(response.json())

#lab04.1.3
# Convert that into a function and call it from inside a if __name__ ==“__main__”:

def readbooks():
    response = requests.get(URL)
    return response.json()

# if __name__ == "__main__":
   # print(readbooks())

#lab04.1.4
# Write the function for find by id and test it (you need to write the testing code)

def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    #return response.status_code
    return response.json()

# if __name__ == "__main__":
   # print(readbook(163))

#lab4.1.5 write code to create a book and test it (you ned to write your own testing code)#

def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

# lab04.1.6 write the update function
def updatebook(id, update):
    urltoupdate = URL + "/" + str(id)
    response = requests.put(urltoupdate, json = update)
    return response.json()

#lab04.1.7 write the delete function
def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

# Have you tested all of these; below are all the functions tested:
if __name__ == "__main__":
    book = {
        'Author':'TestAuthor',
        'Price': 56789,
        'Title':'TestBook'
    }

    update = {
        'Author': 'TheWriterOfTheBook',
        'Title': 'PracticingREQUESTS'
    }
    #print(createbook(book))
    #print(updatebook(340,update))
    #print(deletebook(340))
    print(readbooks())
    print(readbook(195))