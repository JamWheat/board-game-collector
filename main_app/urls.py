from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games_index, name='index'),
  path('games/<int:game_id>/', views.games_detail, name='detail'),
  path('games/create/', views.GameCreate.as_view(), name='games_create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
  path('games/<int:game_id>/add_play/', views.add_play, name='add_play'),
  path('games/<int:game_id>/assoc_exp/<int:expansion_id>/', views.assoc_exp, name='assoc_exp'),
  # expansions
  path('expansions/', views.ExpansionList.as_view(), name='expansions_index'),
  path('expansions/<int:pk>/', views.ExpansionDetail.as_view(), name='expansions_detail'),
  path('expansions/create/', views.ExpansionCreate.as_view(), name='expansions_create'),
  path('expansions/<int:pk>/update/', views.ExpansionUpdate.as_view(), name='expansions_update'),
  path('expansions/<int:pk>/delete/', views.ExpansionDelete.as_view(), name='expansions_delete'),
  
]