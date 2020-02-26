import datetime
from typing import Dict

import jwt
from flask import jsonify, request, Response

# from bookModel import *
# from settings import *

from pluralsight.flask.BookModel import *

from pluralsight.flask.settings import *

app.config['SECRET_KEY'] = 'meow'


def is_book_valid(book: Dict[str, any]) -> bool:
    if ("isbn" in book
            and "price" in book
            and "name" in book):
        return True
    else:
        return False


@app.route('/login')
def get_token():
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token


@app.route('/')
def welcome():
    return "Welcome to my Books API application!"


# Get /books
@app.route('/books')
def get_books():
    print('get books')
    return jsonify({'books': Book.get_all_books()})


# Get
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    find_book = Book.get_book(isbn)
    return jsonify(find_book)


# POST
@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if is_book_valid(request_data):
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        response = Response(json.dumps(''), 201, mimetype="application/json")
        response.headers['Location'] = '/books/' + str(request_data['isbn'])
        return response
    else:
        invalid_book_object_error_msg = {
            "error": "Invalid book object passed in request",
            "helpString": "bla bla bla"
        }
        response = Response(json.dumps(invalid_book_object_error_msg), status=400, mimetype="application/json")
        return response


# PUT
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    Book.replace_book(isbn, request_data['name'], request_data['price'])

    response = Response("", status=204)
    return response


# PATCH
@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    if "name" in request_data:
        Book.update_book(isbn, request_data['name'])
    if "price" in request_data:
        Book.update_book(isbn, request_data['price'])
    response = Response("", 204)
    response.headers['Location'] = '/books/' + str(id)
    return response


# DELETE
# I'm too lazy to do that :(
