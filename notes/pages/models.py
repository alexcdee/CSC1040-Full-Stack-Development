from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True) # Avoid duplicates
    year_published = models.IntegerField()
    summary = models.TextField()
    out_of_print = models.BooleanField(default=False)
    # This creates the author_id foreign key column
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title