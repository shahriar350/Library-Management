from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django import forms

# code here
from django.core.exceptions import ValidationError


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            f"{value} is taken.",
            params={'value': value}
        )


class UserForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
