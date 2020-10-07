from django.db import models
from django.urls import reverse

# Create your models here.
PLAYERS = (
  ('1', '1 player'),
  ('2', '2 players'),
  ('3', '3 players'),
  ('4', '4 players'),
  ('5', '5 players'),
  ('6', '6 players'),
  ('7', '7 players'),
  ('8', '8 players'),
  ('+', 'More than 8 players'),
)

RATING = (
  ('1', '1 star'),
  ('2', '2 stars'),
  ('3', '3 stars'),
  ('4', '4 stars'),
  ('5', '5 stars'),
)

class Game(models.Model):
  name = models.CharField(max_length=100)
  publisher = models.CharField(max_length=100)
  designer = models.CharField(max_length=100)
  pub_year = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={"game_id": self.id})

class Play(models.Model):
  date = models.DateField()
  num_players = models.CharField(
    ("Number of Players"),
    max_length=1,
    choices=PLAYERS,
    default=PLAYERS[0][0]
  )
  rating = models.CharField(
    max_length=1,
    choices=RATING,
    default=RATING[2][0]
  )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return f'Played on {self.date}'
  
