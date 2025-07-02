from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
usename = 'admin'
password = '1234'


@app.route('/')  # localhost:5001
def home():
    #return "Hello, World!"
    return render_template('home.html')



login_page = '''
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="POST">
  <label>Username:</label><br>
  <input type="text" name="username"><br><br>
  <label>Password:</label><br>
  <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
<p style="color:red;">{{ error }}</p>
'''

welcome_page = '''
<!doctype html>
<title>Welcome</title>
<h2>Welcome, {{ user }}!</h2>
'''


@app.route('/login', methods=['GET', 'POST'])  # localhost:8000/login
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('loginvalidation', username=username, password=password))
    return render_template('login.html')

@app.route('/register')  # localhost:5000/register
def register():
    return 'register page'


@app.route('/loginvalidation/<username>/<password>') 
# localhost:5000/loginvalidation/admin/admin
def loginvalidation(username, password):
    if username == "admin" and password == "admin":
        return redirect(url_for('predict'))
    elif username == "user" and password == "user":
        return redirect(url_for('predict'))
    else:
        return 'invalid %s' % username
    
@app.route('/admin')
def adminpage():
    return '<h1>Admin Home Page</h1>'

@app.route('/user')
def userpage():
    return '<h1><center>User Home Page</center></h1>'

@app.route('/printname/<uname>')  # localhost:5000/printname/sandy
def printname(uname):
    return 'Your name: %s' % uname



       
import pickle
model = pickle.load(open('model.pkl','rb'))
@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    return render_template('predict.html')

@app.route('/prediction',methods=['POST']) 
def prediction():
    int_feature=[x for x in request.form.values()]
    print(int_feature)
    int_feature=[float(i) for i in int_feature]
    final_feature=[np.array(int_feature)]
    
    
    prediction=model.predict(final_feature)
    output=format(prediction[0])
    print(output)
    return render_template('predict.html',prediction_text=output)

            
    
    
    
    
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)