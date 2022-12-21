from django.urls import path

from words.views import index, view_word

urlpatterns = [
    path('', index, name='add_word'),
    path('view_word/', view_word, name='view_word'),
]
