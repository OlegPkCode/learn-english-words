from django.contrib import admin
from .models import Categories, Dictionaries, Words


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class DictionariesAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    search_fields = ('name', 'url')


class WordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'time_create', 'time_clear', 'category_id')
    list_display_links = ('word', )
    search_fields = ('word', )
    list_filter = ('time_create', 'time_clear')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Dictionaries, DictionariesAdmin)
admin.site.register(Words, WordsAdmin)
