from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Dictionaries(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'


class Words(models.Model):
    word = models.CharField(max_length=200, unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_clear = models.DateTimeField(null=True)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
