from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome', 
        'quantidade', 
        'lab_usado',
        'patrimonio',
        'show',
        )
    ordering = (
        '-id',
        )
    search_fields = ('id', 'nome', 'lab_usado', 'patrimonio')
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ('id', 'nome')
    list_editable = 'show',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
   
    list_per_page = 10
  
    ordering = (
        '-id',
    )