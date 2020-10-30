from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import School



class SchoolRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #schoolname = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super(SchoolRegisterForm, self).save(commit=False)
    #     user.schoolname = self.cleaned_data["schoolname"]
    #     if commit:
    #         user.save()
    #     return user


# class SchoolProfileForm(forms.ModelForm):
#     class Meta:
#         model = School
#         fields = ['name', 'code', 'region']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class SchoolUpdateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        exclude = ['user']