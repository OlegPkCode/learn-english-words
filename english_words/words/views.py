from datetime import datetime
from django.shortcuts import render, redirect
from .models import Words
from .forms import AddWordForm

menu = ["Изучаемые слова", "Статистика",
        "Настройки", "Обратная связь", "Войти"]


def add_word(request):
    words_list = Words.objects.filter(time_clear__isnull=True)
    # words_list = Words.objects.all()
    form = AddWordForm(initial={'category_id': 1})
    form.fields['category_id'].initial = 1

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
        'form': form,
    }

    return render(request, 'words/add_word.html', context=context)


def view_word(request, word_id):
    word_item = Words.objects.get(pk=word_id)

    if 'clear_word' in request.POST:
        w = Words.objects.get(pk=word_id)
        w.time_clear = datetime.now()
        w.save()
        return redirect('add_word')
    elif 'delete_word' in request.POST:
        return redirect('confirm_delete_word', word_id=word_id)

    context = {'menu': menu, 'title': 'Слово', 'word_item': word_item}

    return render(request, 'words/view_word.html', context=context)


def confirm_delete_word(request, word_id):
    word_item = Words.objects.get(pk=word_id)

    if 'delete_word' in request.POST:
        w = Words.objects.get(pk=word_id)
        w.delete()
        return redirect('add_word')
    elif 'cancel_delete' in request.POST:
        return redirect('add_word')

    context = {'menu': menu, 'title': 'Слово', 'word_item': word_item}

    return render(request, 'words/confirm_delete_word.html', context=context)
