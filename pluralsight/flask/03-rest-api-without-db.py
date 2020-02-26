import json

from flask import Flask, jsonify, request, Response

app = Flask(__name__)

books = [
    {
        "id": 1,
        "author": "Chinua Achebe",
        "title": "Things Fall Apart",
    },
    {
        "id": 2,
        "author": "Hans Christian Andersen",
        "title": "Fairy tales"
    },
    {
        "id": 3,
        "author": "Dante Alighieri",
        "title": "The Divine Comedy",
    },
    {
        "id": 4,
        "author": "Unknown",
        "title": "The Epic Of Gilgamesh",
    }]


def is_book_valid(book):
    if ("id" in book
            and "author" in book
            and "title" in book):
        return True
    else:
        return False


@app.route('/')
def welcome():
    return "Welcome to my Books API application!"


# Get
@app.route('/books')
def get_books():
    print('get books')
    return jsonify({'books': books})


# Get
@app.route('/books/<int:id>')
def get_book_by_id(id):
    find_book = {}
    for book in books:
        if book['id'] == id:
            find_book = book
    return jsonify(find_book)


# POST
@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if is_book_valid(request_data):
        new_book = {
            'id': request_data['id'],
            'author': request_data['author'],
            'title': request_data['title']
        }
        books.append(new_book)
        response = Response(json.dumps(new_book), 201, mimetype="application/json")
        response.headers['Location'] = '/books/' + str(new_book['id'])
        return response
    else:
        invalid_book_object_error_msg = {
            "error": "Invalid book object passed in request",
            "helpString": "bla bla bla"
        }
        response = Response(json.dumps(invalid_book_object_error_msg), status=400, mimetype="application/json")
        return response


# PUT
@app.route('/books/<int:id>', methods=['PUT'])
def replace_book(id):
    request_data = request.get_json()
    new_book = {
        'author': request_data['author'],
        'title': request_data['title'],
        'id': id
    }
    i = 0
    for book in books:
        current_id = book['id']
        if current_id == id:
            books[i] = new_book
            i += 1
    response = Response("", status=204)
    return response


# PATCH
@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    request_data = request.get_json()
    updated_book = {}
    if "title" in request_data:
        updated_book['title'] = request_data['title']
    if "author" in request_data:
        updated_book['author'] = request_data['author']
    for book in books:
        if book['id'] == id:
            book.update(updated_book)
    response = Response("", 204)
    response.headers['Location'] = '/books/' + str(id)
    return response


# DELETE
# I'm too lazy to do that :(
