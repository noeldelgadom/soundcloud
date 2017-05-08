from django import forms
from songs.models import Song

class NewSongForm(forms.ModelForm):
    class Meta():
        model = Song
        fields = '__all__'
