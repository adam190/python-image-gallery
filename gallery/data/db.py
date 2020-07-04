import psycopg2
import json
from gallery.ui.secrets import get_secret_image_gallery

db_name = "image_gallery"
connection = None

def get_secret():
    jsonString = get_secret_image_gallery()
    return json.loads(jsonString)

def get_password(secret):
    return secret['password']

def get_host(secret):
    return secret['host']

def get_username(secret):
    return secret['username']

def get_dbname(secret):
    return secret['db_name']

def connect():
    global connection
    secret = get_secret()
    connection = psycopg2.connect(host=get_host(secret), database = get_dbname(secret), user=get_username(secret), password=get_password(secret))
    connection.set_session(autocommit=True)

def execute(query, args=None):
    global connection
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    return cursor

def list_user():
    global connection
    res = execute('select * from users')
    for row in res:
        print(row)


def add_user():
    global connection
    x = str(input("Username>"))
    y = str(input("Password>"))
    z = str(input("Full name>"))

    res = execute("insert into users (username, password, full_name) values (%s, %s, %s)", (x, y, z))

    return res


def edit_user():
    global connection
    x = str(input("Username to edit>"))
    y = str(input("New password (press enter to keep current)>"))
    z = str(input("New full name (press enter to keep current)>"))

    res = execute("update users set password=%s, full_name=%s where username=%s", (y, z, x))
    return res


def delete_user():
    global connection
    x = str(input("Enter username to delete>"))
    y = str(input("Are you sure you want to delete " + x + "? "))
    if y == 'Yes' or 'Y' or 'y' or 'yes':
        res = execute("delete from users where username=%s", (x,))
        print('Deleted.')

    return res


def quitting():
    print('Bye')


def main():
    connect()
    res = execute('select * from users')
    for row in res:
        print(row)
    while True:
        print("1) List users\n2) Add user\n3) Edit user\n4) Delete user\n5) Quit")
        x = int(input("Enter Command>"))
        if x == 1:
            list_user()
        elif x == 2:
            add_user()
        elif x == 3:
            edit_user()
        elif x == 4:
            delete_user()
        elif x == 5:
            quitting()
            break 


if __name__ == '__main__':
    main()
