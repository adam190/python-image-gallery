from flask import Flask
from flask import request
from flask import render_template
from gallery.ui import db
from flask import redirect
from ..data.useer import user
from ..data.postgres_user_dao import PostgresUserDAO
from ..data.db import connect

app = Flask(__name__)
app.secret_key = b'lkj;alsdkjf'
connect()

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Hello</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Select a link below:</h1>
    </body>
</html>
"""

@app.route('/goodbye')
def goodbye():
    return 'Goodbye'

@app.route('/greet/<name>')
def greet(name, foo, bar):
    return 'Nice to meet you ' + name

@app.route('/add/<int:x>/<int:y>', methods = ['Get'])
def add(x,y):
    return 'The sum is ' + str(x + y) 

@app.route('/mult')
def mult():
    x = request.args['x']
    y = request.args['y']
    return 'The product is ' + str(int(x)*int(y))

@app.route('/calculator/<personsName>')
def calculator(personsName):
   return render_template('calculator.html', name=personsName)

@app.route('/admin')
def admin():
    users = list_user()
    return render_template('admin.html', users=users)

@app.route('/admin/listUser')
def listUser():
    users = list_user()
    return render_template('listUser.html', users=users)

@app.route('/admin/addUser', methods=["GET", "POST"])
def addUser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        add_user(username, password, fullname)
    return render_template('addUser.html')

@app.route('/admin/editUser/<string:user>/<string:password>/<string:fullname>')
def editUser():
    edit_user(user, password, fullname)

    return render_template('editUser.html', user=user, password=password, fullname=fullname)

@app.route('/admin/deleteUser')
def deleteUser(username):
    delete_user(username)
    return render_template('deleteUser.html')


