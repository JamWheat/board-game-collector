from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Game, Expansion
from .forms import PlayForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  expansions_game_doesnt_have = Expansion.objects.exclude(id__in = game.expansions.all().values_list('id'))
  play_form = PlayForm()
  return render(request, 'games/detail.html', { 
    'game': game,
    'play_form': play_form,
    'expansions': expansions_game_doesnt_have
  })

def add_play(request, game_id):
  form = PlayForm(request.POST)
  if form.is_valid():
    new_play = form.save(commit=False)
    new_play.game_id = game_id
    new_play.save()
  return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

class ExpansionList(ListView):
  model = Expansion

class ExpansionDetail(DetailView):
  model = Expansion

class ExpansionCreate(CreateView):
  model = Expansion
  fields = '__all__'

class ExpansionUpdate(UpdateView):
  model = Expansion
  fields = ['title', 'pub_year']

class ExpansionDelete(DeleteView):
  model = Expansion
  success_url = '/expansions/'

def assoc_exp(request, game_id, expansion_id):
  Game.objects.get(id=game_id).expansions.add(expansion_id)
  return redirect('detail', game_id=game_id)