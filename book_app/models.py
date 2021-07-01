from django.db import models


# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(BookCategory,related_name='rel_book_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


