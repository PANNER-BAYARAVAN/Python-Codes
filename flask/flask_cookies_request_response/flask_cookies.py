from flask import Flask, redirect, url_for, request,make_response
app = Flask(__name__)


@app.route('/teacher')
def teacher():
    name = request.cookies.get('userID')
    return name

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
       user = request.form['nm']
       resp=make_response(redirect(url_for('teacher')))
       resp.set_cookie('userID', user)
   
   return resp

if __name__ == '__main__':
   app.run()
