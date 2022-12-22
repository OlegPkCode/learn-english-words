from django.urls import path

from words.views import add_word, view_word, confirm_delete_word

urlpatterns = [
    path('', add_word, name='add_word'),
    path('view_word/<int:word_id>', view_word, name='view_word'),
    path('confirm_delete_word/<int:word_id>', confirm_delete_word, name='confirm_delete_word'),
]
