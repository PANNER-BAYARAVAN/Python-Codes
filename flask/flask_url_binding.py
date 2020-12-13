from flask import Flask,redirect,url_for

app = Flask(__name__)
@app.route('/teacher')
def hello_teacher():
    return 'Hey Teacher'

@app.route('/hello_students')
def hello_students():
    return 'Hey Students'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'teacher':
        return redirect('http://google.com',code=302)
    else:
        return redirect(url_for('hello_students'))

if __name__ == "__main__":
    app.run(debug = True)
