from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
   return 'Index!'
 
@app.route('/hello')
def hello():
    return 'Hello World!'
 
@app.route('/members')
def members():
    return 'Members'

if __name__ == "__main__":
    app.run()
