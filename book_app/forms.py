from django import forms

from book_app.models import BookCategory, Book


class CategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','category']
