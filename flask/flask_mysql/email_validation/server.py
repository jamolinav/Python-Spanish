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
    return redirect('/emails')

@app.route('/emails')
def users():
    mysql = connectToMySQL('first_flask')
    emails = mysql.query_db('SELECT * FROM emails;')
    print(emails)
    return render_template('index.html', accion='emails', all_emails=emails)

@app.route('/user/<email>')
def show(email):
    mysql = connectToMySQL('first_flask')
    sql = 'SELECT * FROM emails WHERE email = %(email)s;'
    data = {
        'email' : email
    }
    email = mysql.query_db(sql, data)
    if len(email) == 1:
        print(email)
        email = email[0]
    return render_template('index.html', accion='show', email=email)

@app.route('/email/<email>/edit')
def edit(email):
    mysql = connectToMySQL('first_flask')
    sql = 'SELECT * FROM emails WHERE email = %(email)s;'
    data = {
        'email' : email
    }
    email = mysql.query_db(sql, data)
    if len(email) == 1:
        print(email)
        email = email[0]
    return render_template('index.html', accion='edit', email=email)

@app.route('/email/<email>/update', methods=['POST'])
def update(email):
    print(request.form)
    email       = request.form['email']
    is_valid = True
    if valMail(email) == False:
        is_valid = False
        flash("Invalid email address!")
    session['email']   = email
    if not is_valid:
        return redirect('/emails')
    session['email']   = ''
    
    mysql = connectToMySQL('first_flask')
    sql = 'UPDATE emails SET email = %(email)s WHERE id = %(email)s;'
    data = {
        'email' : email
    }
    email = mysql.query_db(sql, data)
    print(email)
    return redirect('/emails')

@app.route('/email/new_email')
def new():
    return render_template('index.html', accion='new')

@app.route('/email/create', methods=['POST'])
def insert():
    print(request.form)
    email       = request.form['email']
    is_valid = True
    if valMail(email) == False:
        is_valid = False
        flash("Invalid email address!")

    session['email']   = email
    if not is_valid:
        return redirect('/emails')

    sql = 'SELECT * FROM emails WHERE email = %(email)s;'
    data = {
        'email' : email
    }

    mysql = connectToMySQL('first_flask')
    email_transac = mysql.query_db(sql, data)
    print(email_transac)
    if len(email_transac) > 0:
        flash("Email ya existe!")
        return redirect('/emails')

    session['email']   = ''
    
    sql = 'INSERT INTO emails (email,created_at) VALUES(%(email)s, now());'
    data = {
        'email' : email
    }
    mysql = connectToMySQL('first_flask')
    email_t = mysql.query_db(sql, data)
    if email_t == 0:
        print(f'Email ingresado correctamente: {email}')
        flash(f'Email ingresado correctamente: {email}')
    else:
        print(f'Error al ingresar registro en la BDD: {email}')
        flash(f'Error al ingresar registro en la BDD: {email}')
    print(email_t)
    return redirect('/emails')

@app.route('/email/<email>/destroy')
def delete(email):
    mysql = connectToMySQL('first_flask')
    sql = 'DELETE FROM emails WHERE email = %(email)s;'
    data = {
        'email' : email
    }
    flash(f'Email eliminado de la BDD: {email}')
    email = mysql.query_db(sql, data)
    print(email)
    return redirect('/emails')

if __name__ == "__main__":
    app.run(debug=True)
