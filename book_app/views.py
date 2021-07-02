import ujson
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from book_app.forms import CategoryForm, BookForm, AuthorForm
from book_app.models import BookCategory, Book, Author


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/new/')
    else:
        form = BookForm()
    books = Book.objects.prefetch_related('category').all()
    return render(request, 'books/create.html', {'form': form, 'books': books})


def category(request):
    if request.is_ajax():
        categories = list(BookCategory.objects.values('name'))
        return HttpResponse(ujson.dumps(categories), content_type='application/json')
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/category/')
    else:
        form = CategoryForm()
    return render(request, 'books/category.html', {'form': form})


def all_books(request):
    if request.is_ajax():
        books = list(Book.objects.all())
        arr = []
        for book in books:
            temp = {'name': book.name, 'category': [], 'author': []}
            if len(book.category.all()) > 0:
                for cat in book.category.all():
                    temp['category'].append(cat.name)
            if len(book.author.all()) > 0:
                for author in book.author.all():
                    temp['author'].append(author.name)
            arr.append(temp)
        return HttpResponse(ujson.dumps(arr), content_type='application/json')


def author_all(request):
    if request.is_ajax():
        authors = Author.objects.prefetch_related('author_books').all()
        arr = []
        for author in authors:
            temp = {'name': author.name, 'book': []}
            if len(author.author_books.all()) > 0:
                for book in author.author_books.all():
                    temp['book'].append(book.name)
            arr.append(temp)
        return HttpResponse(ujson.dumps(arr), content_type='application/json')
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/author/')
        pass
    else:
        form = AuthorForm()
    return render(request, 'books/author.html', {'form': form})
