from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

#from ..data.user import User
#from ..data.postgres_user_dao import PostgresUserDAO
from .tools.db import connect 

app = Flask(__name__)

app.secret_key = b'lkj;alsdkjf'
connect()

def get_user_dao():
	return PostgresUserDAO()

@app.route('/users')
def users():
    result = ""
    for user in get_user_dao().get_users():
        result += str(user)
    return result

@app.route('/inc')
def inc():
    if 'value' not in session:
        sessions['value'] =0
    session['value'] = session['value'] + 1
    return "<h1>"+str(session['value'])+"</h1>"

@app.route('/storeStuff')
def storeStuff():
	session['session'] = 22
	session['other things'] = 'bob'

@app.route('/debugSession')
def debugSession():
	result = ""
	for key,value in session.items():
		result += key+"->"+str(value)+"<br />"
	return result

@app.route('/admin/executeDeleteUser/<username>')
def executeDeleteUser(username):
	get_user_dao().delete_user(username)
	return redirect('/admin/users')

@app.route('/admin/deleteUser/<username>')
def deleteUser(username):
	return render_template("confirm.html",
				title="Confirm delete",
				message="Are you sure you want to delete this user",
				on_yes="/admin/executeDeleteUser/"+username,
				on_no="/admin/users")

@app.route('/admin/users')
def users():
<<<<<<< HEAD
#	return render_template('users.html, users=get_user_dao().get_users())
	pass
=======
	return render_template('users.html', users=get_user_dao().get_users())
>>>>>>> 696e2c3a90f9df9f0800912a6de568d1f410d0df

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


