from django.shortcuts import render, redirect
from .models import Words
from .forms import AddWordForm

menu = ["Изучаемые слова", "Статистика",
        "Настройки", "Обратная связь", "Войти"]


def index(request):
    words_list = Words.objects.all()
    form = AddWordForm()

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_word')
    else:
        form = AddWordForm()

    context = {
        'menu': menu,
        'title': 'Слова',
        'words': words_list,
        'form:': form
    }
    return render(request, 'words/index.html', context=context)


def view_word(request, word_id):
    word_name = Words.objects.get(pk=word_id)

    word_data = {'word_id': word_id, 'word_name': word_name}
    context = {'menu': menu, 'title': 'Слово', 'word_data': word_data}

    return render(request, 'words/view_word.html', context=context)
