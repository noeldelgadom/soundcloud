from django.conf.urls import url
from songs import views

urlpatterns = [
    url(r'^$', views.index, name='songs_index'),
    url(r'^new/', views.new, name='new_song'),
]
