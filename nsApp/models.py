from django.db import models

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    ratings = models.CharField(max_length=10)
    # One to Many rel to Author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
