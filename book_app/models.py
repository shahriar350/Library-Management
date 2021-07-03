from django.db import models
# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Author(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    name = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(BookCategory, related_name='rel_book_categories')
    author = models.ManyToManyField(Author, related_name='author_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        quantity_update = self.quantity - self.rel_book_borrow.filter(is_returned=False).count()
        return f"Name: {self.name}" + " " + f"ISBN: {self.isbn}" + " " + f'Quantity: {str(quantity_update)}'

    class Meta:
        ordering = ('name',)
