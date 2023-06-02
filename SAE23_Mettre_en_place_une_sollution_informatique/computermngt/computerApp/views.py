from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from computerApp.models import Machine
from computerApp.models import Personnel
from .forms import AddMachineForm
from .forms import AddPersonnelForm
from django.http import HttpResponseForbidden





# Create your views here.
def index(request):
    return render(request, 'index.html', {"date": datetime.today()})


def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines': machines}
    return render(request, 'computerApp/machine_list.html', context)


def personnel_list_view(request) :
    personnes = Personnel.objects.all()
    context={'personnes': personnes}
    return render(request, 'computerApp/personnel_list.html', context)



def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render(request, 'computerApp/machine_detail.html', context)

def personne_detail_view(request, pk):
    personne = get_object_or_404(Personnel, id=pk)
    context={'personne': personne}
    return render(request, 'computerApp/personne_detail.html', context)


@login_required(login_url='/login/')
def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'computerApp/machine_add.html', context)


@login_required(login_url='/login/')
def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personne = Personnel(nom=form.cleaned_data['nom'])
            new_personne.save()
            return redirect('personnes')
    else:
        form = AddPersonnelForm()
        context = {'form': form}
        return render(request, 'computerApp/personne_add.html', context)


# connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_machine')  # Redirect to add machine page after successful login
        else:
            return HttpResponseForbidden('Invalid login credentials')
    else:
        return render(request, 'login.html')


# déconnexion
def logout_view(request):
    logout(request)
    return redirect('index')
