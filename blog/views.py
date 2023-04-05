from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def add_new(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})

