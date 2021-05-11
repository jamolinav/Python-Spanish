from django.db import models

# Create your models here.
 
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f'<Movie object: {self.first_name} {self.last_name} ({self.id})>'