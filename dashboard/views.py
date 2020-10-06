from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student,Staff
from .forms import StudentRegisterForm,StaffRegisterForm

# Create your views here.

def home(request):
    return render(request,'home.html',{})


def dashboard(request):
    student = Student.objects.all()
    staff = Staff.objects.all()
    context = {
        'student':student,
        'staff':staff,
    }
    return render(request,'dashboard.html',context)


def studentreg(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first')
            messages.success(request, f'Student has been created! You can view in the list!')
            return redirect('dashboard')
    else:
        form = StudentRegisterForm()
    return render(request, 'studentregister.html', {'form': form})


def staffreg(request):
    if request.method == 'POST':
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first')
            messages.success(request, f'Staff has been created! You can view in the list!')
            return redirect('dashboard')
    else:
        form = StaffRegisterForm()
    return render(request, 'staffregister.html', {'form': form})