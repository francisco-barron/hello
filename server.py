from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
import re
from datetime import datetime
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "unicorn"
bcrypt = Bcrypt(app)

@app.route('/')
def index():
	return render_template('index.html')





@app.route('/hacker')
def show_hacker():
	return render_template('products.html')




if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)