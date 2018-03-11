from blog.models import Article
from blog.models import Music
from django.contrib import admin
from .models import Newslatter

admin.site.register(Article)
admin.site.register(Music)
admin.site.register(Newslatter)


