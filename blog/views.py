from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def add_new(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect(f'/detail/{instance.id}')

    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', context={'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, request.FILES, instance=employee)
    if form.is_valid():
        form.save()
        return redirect(f'/detail/{id}')
    return render(request, 'update.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')


def detail(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'detail.html', {'employee': employee})
