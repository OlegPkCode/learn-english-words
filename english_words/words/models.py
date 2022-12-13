from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Words(models.Model):
    word = models.CharField(max_length=200, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_clear = models.DateTimeField(blank=True)
    user_id = models.ForeignKey('Users', on_delete=models.PROTECT)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT)


class Dictionaries(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('Users', on_delete=models.PROTECT)
