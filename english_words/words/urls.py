from django.urls import path

from words.views import index

urlpatterns = [
    path('', index, name='add_word'),
]
