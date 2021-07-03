import ujson
from django.db.models import TextField
from django.db.models.functions import Cast
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from student_app.forms import StudentForm, BorrowForm
from student_app.models import Student, Borrow


def new_student(request):
    if request.is_ajax():
        students = list(Student.objects.values('name', 'student_id'))
        return HttpResponse(ujson.dumps(students), content_type='application/json')
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/create/')
    else:
        form = StudentForm()
    return render(request, 'student/create.html', {'form': form})


def borrow_book(request):
    if request.is_ajax():
        borrows = list(Borrow.objects.values('book__name', 'student__name','student__student_id', 'is_returned', date_return=Cast('return_date', TextField())))

        return HttpResponse(ujson.dumps(borrows), content_type='application/json')
    elif request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/borrow/')
    else:
        form = BorrowForm()
    return render(request, 'student/borrow.html', {'form': form})
