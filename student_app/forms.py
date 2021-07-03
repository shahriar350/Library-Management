from django import forms
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.forms import DateInput

from book_app.models import BookCategory, Book, Author
from student_app.models import Student, Borrow


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','student_id']


class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book','student', 'is_returned','return_date']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "This student already taken this book.",
            }
        }
        widgets = {
            'return_date': DateInput(attrs={'type': 'date'})
        }

    def clean_book(self):
        data = self.cleaned_data['book']
        if data.quantity > Borrow.objects.filter(book=data,is_returned=False).values('book').count():
            return data
        else:
            raise ValidationError('This book is not available')




