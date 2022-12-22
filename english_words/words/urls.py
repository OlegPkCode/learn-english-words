from django.urls import path

from words.views import add_word, view_word

urlpatterns = [
    path('', add_word, name='add_word'),
    path('view_word/<int:word_id>', view_word, name='view_word'),
]
