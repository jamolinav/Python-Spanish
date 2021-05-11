from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
import re	# the regex module
# crea un objeto de expresion regular que  vamos a usar despues
def valMail(mail):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    if not EMAIL_REGEX.match(mail):    # prueba si el campo y el patron son iguales
        return False
    return True

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def root():
    return redirect('/users')

@app.route('/users')
def users():
    mysql = connectToMySQL('first_flask')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template('index.html', accion='users', all_users=users)

@app.route('/user/<int:id>')
def show(id):
    mysql = connectToMySQL('first_flask')
    sql = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        'id' : id
    }
    user = mysql.query_db(sql, data)
    if len(user) == 1:
        print(user)
        user = user[0]
    return render_template('index.html', accion='show', user=user)

@app.route('/user/<int:id>/edit')
def edit(id):
    mysql = connectToMySQL('first_flask')
    sql = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        'id' : id
    }
    user = mysql.query_db(sql, data)
    if len(user) == 1:
        print(user)
        user = user[0]
    return render_template('index.html', accion='edit', user=user)

@app.route('/user/<int:id>/update', methods=['POST'])
def update(id):
    print(request.form)
    first_name  = request.form['first_name']
    last_name   = request.form['last_name']
    email       = request.form['email']
    mysql = connectToMySQL('first_flask')
    sql = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = now() WHERE id = %(id)s;'
    data = {
        'id' : id,
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email
    }
    user = mysql.query_db(sql, data)
    print(user)
    return redirect('/users')

@app.route('/user/new_user')
def new():
    return render_template('index.html', accion='new')

@app.route('/user/create', methods=['POST'])
def insert():
    print(request.form)
    first_name  = request.form['first_name']
    last_name   = request.form['last_name']
    email       = request.form['email']
    is_valid = True
    if len(first_name) == 0:
        is_valid = False
        flash("Please enter a first name")
    if len(last_name) == 0:
        is_valid = False
        flash("Please enter a last name")
    if valMail(email) == False:
        is_valid = False
        flash("Invalid email address!")

    session['first_name']   = first_name
    session['last_name']    = last_name
    session['email']   = email
    if not is_valid:
        return redirect('/user/new_user')
    session['first_name']   = ''
    session['last_name']    = ''
    session['email']   = ''

    mysql = connectToMySQL('first_flask')
    sql = 'INSERT INTO users (first_name, last_name, email, created_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, now());'
    data = {
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email
    }
    user = mysql.query_db(sql, data)
    print(user)
    return redirect('/users')

@app.route('/user/<int:id>/destroy')
def delete(id):
    mysql = connectToMySQL('first_flask')
    sql = 'DELETE FROM users WHERE id = %(id)s;'
    data = {
        'id' : id
    }
    user = mysql.query_db(sql, data)
    print(user)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
