from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SchoolRegisterForm(UserCreationForm):
    email = forms.EmailField()
    schoolname = forms.CharField()

    class Meta:
        model = User
        fields = ['schoolname','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SchoolRegisterForm, self).save(commit=False)
        user.schoolname = self.cleaned_data["schoolname"]
        if commit:
            user.save()
        return user