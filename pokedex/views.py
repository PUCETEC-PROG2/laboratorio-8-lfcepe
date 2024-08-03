from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Pokemon ,Trainer
from .forms import Pokemon_Form, Trainer_Form
def index(request):
    pokemons = Pokemon.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id) #pk es una PRIMARY KEY
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def index_trainer(request):
    trainers = Trainer.objects.order_by('name')
    template = loader.get_template('index_trainer.html')
    return HttpResponse(template.render({'trainers': trainers}, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    return render(request, 'display_trainer.html', {'trainer': trainer})

#ADD POKEMON AND TRAINER
@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = Pokemon_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = Pokemon_Form()
        
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = Trainer_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index_trainer')
    else:
        form = Trainer_Form()
    
    return render(request, 'trainer_form.html', {'form': form})

#VIEW LOGIN
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
#EDIT POKEMON AND TRAINER
@login_required
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    if request.method == 'POST':
        form = Pokemon_Form(request.POST,request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index_trainer')
    else:
        form = Pokemon_Form(instance=pokemon)
        
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk = id)
    if request.method == 'POST':
        form = Trainer_Form(request.POST,request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index_trainer')
    else:
        form = Trainer_Form(instance=trainer)
        
    return render(request, 'trainer_form.html', {'form': form})

#DELETE POKEMON AND TRAINER
@login_required
def delete_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    pokemon.delete()
    return redirect("pokedex:index")

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk = id)
    trainer.delete()
    return redirect("pokedex:index_trainer")