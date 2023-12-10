# This file is to create a masic Flask Server for Lab08.04 
# Dapa representation course 2023/24

# By: Eva Czeyda-Pommersheim

from flask import Flask, url_for, request, redirect, abort, jsonify


app = Flask(__name__, static_url_path='', static_folder = 'staticpages')

books = [
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price" : 1000},
    {"id": 2, "Title": "Some travel book", "Author": "Some Author", "Price" : 2000},
    {"id": 3, "Title": "Python made easy", "Author": "More Author", "Price" : 1500}
]
nextId = 4

@app.route('/')
def index():
    return "hello"

# Get all books
# curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
    return jsonify(books)

#find by ID
# curl http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>')
def findById(id):
    foundbooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundbooks) == 0:
        return jsonify(()) , 204
    return jsonify(foundbooks[0])
    

# create
# curl -X "POST" -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"someguy\", \"Price\":123}" http://127.0.0.1:5000/books

@app.route('/books', methods = ['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)

    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price" : request.json["Price"]
    }
    books.append(book)
    nextId+= 1
    return jsonify(book)

# update
# curl -X "PUT" -H "content-type:application/json" -d "{\"Title\":\"new title\", \"Price\":999}" http://127.0.0.1:5000/books/4
@app.route('/books/<int:id>', methods = ['PUT'])
def update(id):
    foundbooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundbooks) == 0:
        return jsonify(()) , 404
    currentBook = foundbooks[0]

    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']
    return jsonify(currentBook)

#delete
# curl -X "DELETE" http://127.0.0.1:5000/books/4
@app.route('/books/<int:id>', methods = ['DELETE'])
def delete(id):
    foundbooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundbooks) == 0:
        return jsonify(()) , 404
    
    books.remove(foundbooks[0])

    return jsonify({"done" : True})


if __name__ == "__main__":
    app.run(debug=True)


