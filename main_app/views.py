from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Game, Expansion
from .forms import PlayForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  expansions_game_doesnt_have = Expansion.objects.exclude(id__in = game.expansions.all().values_list('id'))
  play_form = PlayForm()
  return render(request, 'games/detail.html', { 
    'game': game,
    'play_form': play_form,
    'expansions': expansions_game_doesnt_have
  })

@login_required
def add_play(request, game_id):
  form = PlayForm(request.POST)
  if form.is_valid():
    new_play = form.save(commit=False)
    new_play.game_id = game_id
    new_play.save()
  return redirect('detail', game_id=game_id)

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

class ExpansionList(LoginRequiredMixin, ListView):
  model = Expansion

class ExpansionDetail(LoginRequiredMixin, DetailView):
  model = Expansion

class ExpansionCreate(LoginRequiredMixin, CreateView):
  model = Expansion
  fields = '__all__'

class ExpansionUpdate(LoginRequiredMixin, UpdateView):
  model = Expansion
  fields = ['title', 'pub_year']

class ExpansionDelete(LoginRequiredMixin, DeleteView):
  model = Expansion
  success_url = '/expansions/'

@login_required
def assoc_exp(request, game_id, expansion_id):
  Game.objects.get(id=game_id).expansions.add(expansion_id)
  return redirect('detail', game_id=game_id)