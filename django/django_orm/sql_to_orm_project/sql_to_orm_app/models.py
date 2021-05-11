from django.db import models
import re

# Create your models here.
class dojo(models.Model):
    name    = models.CharField(max_length=255)
    city    = models.CharField(max_length=255)
    state   = models.CharField(max_length=2)
    desc    = models.CharField(max_length=255, default='dojo antiguo')

class ninja(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    dojo        = models.ForeignKey(dojo, related_name='ninjas', on_delete=models.CASCADE)

class Movie(models.Model):
    title       = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration    = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<Movie object: {self.title} ({self.id})>'

class Wizard(models.Model):
    name    = models.CharField(max_length=45)
    house   = models.CharField(max_length=45)
    pet     = models.CharField(max_length=45)
    year    = models.IntegerField()

class Book(models.Model):
	title       = models.CharField(max_length=255)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)
	desc        = models.TextField(default='')

class AuthorManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = 'El nombre debe tener una longitud mayor 1'
        if len(postData['last_name']) < 1:
            errors['last_name'] = 'El apellido debe tener una longitud mayor 1'
        if not re.match('^[A-Za-z_-]*$', postData['first_name']):
            errors['first_name'] = 'El nombre solo puede contener letras'

        return errors

class Author(models.Model):
    first_name  = models.CharField(max_length=45)
    last_name   = models.CharField(max_length=45)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    books       = models.ManyToManyField(Book, related_name='authors')
    notas       = models.CharField(max_length=255, default='')
    objects     = AuthorManager()

class Publisher(models.Model):
	name    = models.CharField(max_length=255)
	books   = models.ManyToManyField(Book, related_name="publishers")
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

class UserManager(models.Manager):
    def validator(self, postData):
        errors  = {}
        if len(postData['name']) < 1:
            errors['name'] = 'Debe ingresar un nombre'
        if len(postData['last_name']) < 1:
            errors['last_name'] = 'Debe ingresar un apellido'
        
        errorsEmail = self.checkEmail(postData['email'])
        if len(errorsEmail) > 0:
            errors['email'] = errorsEmail

        if len(postData['email']) < 1:
            errors['email'] = 'Debe ingresar un email válido'
        if len(postData['password']) < 1:
            errors['password'] = 'Debe ingresar un password válido'

        return errors
    
    def checkEmail(self, email):
        errors  = {}
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9.+_-]+@[A-Za-z0-9.+_-]+\.[A-Za-z]+$')
        if not EMAIL_REGEX.match(email):
            errors['email'] = 'Correo Inválido'
        return errors

class User(models.Model):
    name    = models.CharField(max_length=45)
    last_name   = models.CharField(max_length=45)
    email       = models.CharField(max_length=100)
    password    = models.CharField(max_length=255)
    objects     = UserManager()

