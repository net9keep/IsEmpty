from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'student_id', 'phone_number', 'email', 'password')

class InfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password')