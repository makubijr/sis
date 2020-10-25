from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student,Staff,Grade
from .forms import StudentRegisterForm,StaffRegisterForm

import datetime
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


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
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('dashboard')
    else:
        form = StaffRegisterForm()
    return render(request, 'staffregister.html', {'form': form})


def generate_pdf(request):
    """Generate pdf."""
    # Model data
    grade = Grade.objects.all()
    student = Student.objects.all().order_by('last')

    context = {
        'student': student,
        'grade':grade
    }

    # Rendered
    html_string = render_to_string('pdf-output.html',context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_of_students.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        #output = open(output.name, 'rb')
        response.write(output.read())

    return response


