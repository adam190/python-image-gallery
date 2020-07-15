#import os

#def main():
#    print("hello"+os.getenv("NAME"))

#if __name__ == "__main__":
#    main()

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, world!'
