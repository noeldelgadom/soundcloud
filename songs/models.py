from django.db import models
from music_genres import GENRES
from albums.models import Album
from artists.models import Artist

# Create your models here.
class Song(models.Model):

    track_id = models.AutoField(primary_key=True)
    track_name = models.CharField(max_length=128)
    track_album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    track_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    track_genre = models.CharField(choices=GENRES, max_length=2)

    def __str__(self):
        return self.track_name
