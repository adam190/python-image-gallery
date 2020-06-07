import psycopg2

db_host = "m2-database.ckretnrgsfl4.us-west-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"

connection = None

def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    return result[:-1]

def connect():
    global connection
    connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())
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
    print("1) List Users\n2) Add user\n3) Edit user\n4) Delete user\n5) Quit")
    x = int(input("Enter command>"))
    if x == 1:
        list_user()
    elif x ==2:
        add_user()
        list_user()
    elif x == 3:
        edit_user()
        list_user()
    elif x == 4:
        delete_user()
        list_user()
    elif x == 5:
        quitting()
	
	
if __name__ == '__main__':
    main()
