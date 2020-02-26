from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/serghei.colesnic/Desktop/testing-projects/python/python-lessons/pluralsight/flask/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

