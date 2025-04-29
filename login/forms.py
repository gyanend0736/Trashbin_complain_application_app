from django import forms
from django.contrib.auth.models import User

class Signup(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = User.objects.create_user(username=username, email=email, password=password)
        return user
