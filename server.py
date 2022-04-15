from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/read')

@app.route('/read')
def users():
    users=User.get_all()
    return render_template('read.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/new_user', methods=['post'])
def newUser():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/read')


if __name__ == '__main__':
    app.run(debug=True)