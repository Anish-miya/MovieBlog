from django.db import models


class Music(models.Model):
    id = models.IntegerField(primary_key=True)
    Flim_Name = models.CharField(max_length=32)
    Music_name = models.CharField(max_length=32)


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=3048)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/content/%s/' % self.id


class Newslatter(models.Model):
    Name=models.CharField(max_length=20)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email


class Extra(models.Model):
    Movie_history = models.IntegerField()
    Theater = models.CharField(max_length=32)
    most_wacth = models.CharField(max_length=32)


