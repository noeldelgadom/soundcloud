from django.conf.urls import url
from songs import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
