from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from book_app.forms import CategoryForm, BookForm
from book_app.models import BookCategory, Book


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/new')
    else:
        form = BookForm()
    books = Book.objects.prefetch_related('category').all()
    return render(request, 'books/create.html', {'form': form, 'books': books})


def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/category')
    else:
        form = CategoryForm()
    book_categories = BookCategory.objects.all()
    return render(request, 'books/category.html', {'form': form, 'categories': book_categories})
