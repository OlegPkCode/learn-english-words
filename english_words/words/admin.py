from django.contrib import admin
from .models import Categories, Dictionaries, Words, UserDictionaries


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class DictionariesAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    search_fields = ('name', 'url')


class WordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'time_clear', 'category_id', 'user')
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('time_create', 'time_clear')


class UserDictionariesAdmin(admin.ModelAdmin):
    list_display = ('user', 'dictionary_id')
    list_display_links = ('user', )
    search_fields = ('user', )
    list_filter = ('user', 'dictionary_id')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Dictionaries, DictionariesAdmin)
admin.site.register(Words, WordsAdmin)
admin.site.register(UserDictionaries, UserDictionariesAdmin)