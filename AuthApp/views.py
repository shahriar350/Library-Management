from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UserForm, LoginForm


# Create your views here.
def my_login(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/n1.html")  # Redirect to a success page.
    return render(request, 'auth/login.html', {'form': form})


def my_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                     form.cleaned_data['password'])
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            return HttpResponse('Done')

    else:
        form = UserForm()
    return render(request, 'auth/register.html', {'form': form})
