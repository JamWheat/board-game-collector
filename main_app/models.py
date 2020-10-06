from django.db import models

# Create your models here.
class Game(models.Model):
  name = models.CharField(max_length=100)
  publisher = models.CharField(max_length=100)
  designer = models.CharField(max_length=100)
  pub_year = models.IntegerField()

  def __str__(self):
    return self.name
