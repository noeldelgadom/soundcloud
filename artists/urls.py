from django.conf.urls import url
from artists import views

urlpatterns = [
    url(r'^$', views.index, name='artists_index'),
]
