import time

from django.db import models
from datetime import datetime, timedelta

# Create your models here.
from book_app.models import Book


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.PositiveIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + str(self.student_id)


class Borrow(models.Model):
    book = models.ForeignKey(Book, related_name='rel_book_borrow',on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student,related_name="rel_student_borrow",on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
    return_date = models.DateField(default=datetime.now()+timedelta(days=7))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'student',)

    @property
    def check_book_available(self):
        return self.book.quantity >= Borrow.objects.filter(book=self.book,is_returned=False).count()

    def __str__(self):
        return self.book + " " + self.student
