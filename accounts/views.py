from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SchoolRegisterForm



def register(request):
    if request.method == 'POST':
        form = SchoolRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('dashboard')
    else:
        form = SchoolRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'accounts/profile.html')