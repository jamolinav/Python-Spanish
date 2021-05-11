from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from django.http import JsonResponse
from sql_to_orm_app.models import *
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

# Create your views here.

def index(request):
    return render(request, 'login.html')

def index2(request, s):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def books(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, 'books.html', context)

def add_book(request):
    print(request.POST)
    Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')

def view_book(request, id):
    print(request.GET)
    print('id', id)
    context = {
        'book' : Book.objects.get(id=id),
        'authors' : Author.objects.filter(books=Book.objects.get(id=id)),
        'all_authors' : Author.objects.exclude(books=Book.objects.get(id=id))
    }
    return render(request, 'view_book.html', context)

def add_author(request):
    print(request.POST)
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    if int(author_id) != 0:
        author = Author.objects.get(id=author_id)
        author.books.add(Book.objects.get(id=book_id))
    return redirect(f'/books/{book_id}')

def authors(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def new_author(request):
    print(request.POST)
    errors = Author.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/authors')
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],notas=request.POST['notas'])
    return redirect('/authors')

def view_author(request, id):
    print(request.GET)
    print('id', id)
    author = Author.objects.filter(id=int(id))
    if len(author) > 0:
        context = {
            'author' : Author.objects.get(id=id),
            'books' : Book.objects.filter(authors=Author.objects.get(id=id)),
            'all_books' : Book.objects.exclude(authors=Author.objects.get(id=id))
        }
        return render(request, 'view_author.html', context)
    return redirect('/authors')

def add_book(request):
    print(request.POST)
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    if int(book_id) != 0:
        book = Book.objects.get(id=book_id)
        book.authors.add(Author.objects.get(id=author_id))
    return redirect(f'/authors/{author_id}')

def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        print(request.POST)
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, 'register.html')

        password    = request.POST['password']
        pw_hash     = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        User.objects.create(
            name=request.POST['name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash
        )
        print('new')
        return redirect('/')

def login(request):
    if request.POST == 'GET':
        return render(request, 'login.html')
    else:
        results = User.objects.filter(email=request.POST['email'])
        if results:
            logged_user = results[0]
            pwd_on_bdd  = logged_user.password
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user'] = logged_user.name
                print('logged_user: ', request.session['logged_user'])
                return redirect('/books')
        return redirect('/')

def logout(request):
    try:
        del request.session['logger_user']
    except:
        print('Error')
    return('/')

def checkEmail(request):
    print(request.POST)
    errors = User.objects.checkEmail(request.POST['email'])
    print('errors: ',errors)
    return JsonResponse({'errors' : errors})