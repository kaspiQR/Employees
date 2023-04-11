from django.shortcuts import render, redirect

from .forms import VisitForm
from .models import Visit


def add_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/visits/')
    else:
        form = VisitForm()
    return render(request, 'visits/add_visit.html', {'form': form})


def index(request):
    visits = Visit.objects.all()
    context = {'visits': visits}
    return render(request, 'visits/index.html', context=context)


def detail(request, id):
    visit = Visit.objects.get(id=id)
    context = {'visit': visit}
    return render(request, 'visits/detail_visit.html', context=context)


def delete(request, id):
    Visit.objects.get(id=id).delete()
    return redirect('index_visit')


def edit(request, id):
    visit = Visit.objects.get(id=id)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('/visits/')
    else:
        form = VisitForm(instance=visit)
    return render(request, 'visits/visit_edit.html', {'form': form, 'visit': visit})
