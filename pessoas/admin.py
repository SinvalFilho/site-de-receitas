from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome',)
    list_filter = ('nome',)
    list_per_page = 5

admin.site.register(Pessoa, ListandoPessoas)
