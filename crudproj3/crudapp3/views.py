from django.shortcuts import render,redirect
from crudapp3.models import Person
from crudapp3.forms import RegForm
# Create your views here.
def home(request):
    person = Person.objects.all()
    return render(request, 'home.html', {'person': person})

def create(request):
    form = RegForm()
    if request.method == "POST":
        formt = RegForm(request.POST)
        if formt.is_valid():
            formt.save()
            return redirect('/home')
    return render(request, 'create.html', {'form': form})

def delete(request,id):
    delit = Person.objects.get(id=id)
    delit.delete()
    return redirect('/home')

def edit(request,id):
    edits = Person.objects.get(id=id)
    if request.method == "POST":
        form = RegForm(request.POST, instance = edits)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'edit.html', {'edit': edits})