from django.shortcuts import render
from .models import Words

menu = ["Изучаемые слова", "Статистика",
        "Настройки", "Обратная связь", "Войти"]


def index(request):
    words_list = Words.objects.all()
    return render(request, 'words/index.html', {'menu': menu, 'title': 'words', 'words': words_list})
