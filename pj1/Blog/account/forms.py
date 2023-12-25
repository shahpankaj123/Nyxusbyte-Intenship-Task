from django import forms
from .models import User
import re

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','name','password']

    def clean_email(self):
        email_value = self.cleaned_data['email']
        if len(email_value) < 3:
            raise forms.ValidationError('Email must be at least 3 characters long.')
        return email_value

    def clean_password(self):
        password_value = self.cleaned_data['password']
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:,<.>]).{8,}$')
        if not password_pattern.match(password_value):
            raise forms.ValidationError('Please set a Strong Password')
        return password_value

  
class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())