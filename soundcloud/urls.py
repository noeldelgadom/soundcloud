from django.conf.urls import url, include
from django.contrib import admin
from albums import views, urls as albums_urls
from artists import views, urls as artists_urls
from songs import views, urls as songs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^albums/', include(albums_urls)),
    url(r'^artists/', include(artists_urls)),
    url(r'^songs/', include(songs_urls)),
]
