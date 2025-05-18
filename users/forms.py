from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[("student", "Student"), ("professor", "Professor"), ("admin", "Admin")])

    class Meta:
        model = CustomUser
        fields = ["username", "email", "role", "password1", "password2"]