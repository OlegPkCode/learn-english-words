from datetime import datetime
from django.shortcuts import render, redirect
from .models import Words, Categories
from .forms import AddWordForm


def add_word(request):
    words_list = Words.objects.filter(time_clear__isnull=True)

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_word')
    else:
        form = AddWordForm()

    context = {
        'title': 'Слова',
        'words': words_list,
        'form': form,
    }

    return render(request, 'words/add_word.html', context=context)


def view_word(request, word_id):
    word_item = Words.objects.get(pk=word_id)
    form = AddWordForm()

    if 'clear_word' in request.POST:
        if word_item.time_clear is None:
            word_item.time_clear = datetime.now()
        word_item.save()
        return redirect('add_word')
    elif 'study_word' in request.POST:
        Words.objects.filter(pk=word_id).update(time_clear=None)
        return redirect('add_word')
    elif 'delete_word' in request.POST:
        return redirect('confirm_delete_word', word_id=word_id)

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            word_item.name = form.data['name']
            word_item.category_id = Categories.objects.get(pk=form.data['category_id'])
            word_item.save()
            return redirect('add_word')
    else:
        form = AddWordForm()

    context = {
        'title': 'Слово',
        'word_item': word_item,
        'form': form,
    }

    return render(request, 'words/view_word.html', context=context)


def learned_words(request):
    words_list = Words.objects.filter(time_clear__isnull=False)

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learned_words')
    else:
        form = AddWordForm()

    context = {
        'title': 'Слова',
        'words': words_list,
        'form': form,
    }

    return render(request, 'words/learned_words.html', context=context)


def confirm_delete_word(request, word_id):
    word_item = Words.objects.get(pk=word_id)

    if 'delete_word' in request.POST:
        word_item.delete()
        return redirect('add_word')
    elif 'cancel_delete' in request.POST:
        return redirect('add_word')

    context = {'title': 'Слово', 'word_item': word_item}

    return render(request, 'words/confirm_delete_word.html', context=context)
