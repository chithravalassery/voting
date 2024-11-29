from django.db import models


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=35)
   
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.IntegerField()
    
