from django.shortcuts import render, redirect
from apps.blog_app.lib.mysqlconnection import connectToMySQL
import re
# Create your vie

def valMail(mail):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    if not EMAIL_REGEX.match(mail):    # prueba si el campo y el patron son iguales
        return False
    return True

def root(request):
    return redirect('/blogs/login')

def login(request):
    print('request: {}'.format(request))
    return render(request, 'blog_app/login.html')

def users(request):
    print('request: {}'.format(request.POST))
    mysql = connectToMySQL('first_flask')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    context = {
        'accion' : 'users',
        'all_users' : users
    }
    return render(request, 'blog_app/index.html', context)

def show(request, id):
    print('SHOW....')
    mysql = connectToMySQL('first_flask')
    sql = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        'id' : id
    }
    user = mysql.query_db(sql, data)
    print('show:', user)
    if len(user) == 1:
        print(user)
        user = user[0]
    context = {
        'accion' : 'show',
        'user' : user
    }
    print(user)
    return render(request, 'blog_app/index.html', context)

def edit(request, id):
    mysql = connectToMySQL('first_flask')
    sql = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        'id' : id
    }
    user = mysql.query_db(sql, data)
    if len(user) == 1:
        print(user)
        user = user[0]
    context = {
        'accion' : 'edit',
        'user' : user
    }
    return render(request, 'blog_app/index.html', context)

def update(request, id):
    print(request)
    first_name  = request.POST['first_name']
    last_name   = request.POST['last_name']
    email       = request.POST['email']
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
    return redirect('/blogs/users')

def new(request):
    context = {'accion':'new'}
    return render(request, 'blog_app/index.html', context)

def insert(request):
    print(request)
    first_name  = request.POST['first_name']
    last_name   = request.POST['last_name']
    email       = request.POST['email']
    is_valid = True
    if len(first_name) == 0:
        is_valid = False
    if len(last_name) == 0:
        is_valid = False
    if valMail(email) == False:
        is_valid = False

    request.session['first_name']   = first_name
    request.session['last_name']    = last_name
    request.session['email']   = email
    if not is_valid:
        return redirect('/blogs/user/new_user')
        
    request.session['first_name']   = ''
    request.session['last_name']    = ''
    request.session['email']   = ''

    mysql = connectToMySQL('first_flask')
    sql = 'INSERT INTO users (first_name, last_name, email, created_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, now());'
    data = {
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email
    }
    user = mysql.query_db(sql, data)
    return redirect('/blogs/users')

def delete(request, id):
    mysql = connectToMySQL('first_flask')
    sql = 'DELETE FROM users WHERE id = %(id)s;'
    data = {
        'id' : id
    }
    user = mysql.query_db(sql, data)
    print(user)
    return redirect('/blogs/users')

