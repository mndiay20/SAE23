from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from computerApp.models import Machine
from computerApp.models import Personnel
from django.shortcuts import get_object_or_404
from .forms import AddMachineForm
from .forms import AddPersonnelForm





# Create your views here.


def index(request) :
    # Ajout de la ligne de recupération des machines
    #machines = Machine.objects.all()

    #Trier les machines selo un champ particulier
    #machines = Machine.objects.order_by('-id')

    context = {
    #   'machines' : machines,
    }

    return render(request, 'index.html', context)


def index(request) :
    context = {}
    return render(request, 'templates/index.html', context={"date": datetime.today()})


#authentificatio
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
        else:
            messages.success(request, ("Vos identifiants sont invalides"))
            return redirect('login')
        
    else:
        return render(request, 'authenticate/login.html', {}) 
       




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

def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        form = AddPersonnelForm()
        context = {'form': form}
        return render(request, 'computerApp/personne_add.html', context)