from django.conf.urls import url
from albums import views

urlpatterns = [
    url(r'^$', views.index, name='albums_index'),
]
