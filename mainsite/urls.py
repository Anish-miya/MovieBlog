from django.contrib import admin
from blog import views
from django.conf.urls import include, url

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^about/$', views.about, name='about'),
   url(r'^components/$', views.components, name='components'),
   url(r'^news/$', views.news, name='news'),
   url(r'^$', views.index, name='index'),
   url(r'^song/$', views.song, name='song'),
   url(r'^FB/$', views.FB, name='FB'),
]
