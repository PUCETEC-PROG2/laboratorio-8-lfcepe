from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Pokemon
from .forms import Pokemon_Form
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

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
@login_required
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    if request.method == 'POST':
        form = Pokemon_Form(request.POST,request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = Pokemon_Form(instance=pokemon)
        
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    pokemon.delete()
    return redirect("pokedex:index")