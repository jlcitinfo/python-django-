"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm

# Create your models here.

class Artist(models.Model):
    name = models.CharField('artist',max_length=50)
    year_initial_carrier = models.PositiveIntegerField()

class ArtistForm(ModelForm):
    class Meta:
        model = Artist;
        fields = ['name', 'year_initial_carrier'];
        
class Films(models.Model):
    name = models.CharField('films/series',max_length=50)
    artist = models.ForeignKey(Artist)