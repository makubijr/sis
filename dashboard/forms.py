from django import forms
from .models import Student,Staff

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first', 'last', 'regid', 'grade']

class StaffRegisterForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first', 'last','empid','phone','email']