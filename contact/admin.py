from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name', 
        'quantidade', 
        'lab_used',
        'patrimonio',
        'show',
        )
    ordering = (
        '-id',
        )
    search_fields = ('id', 'name', 'lab_used', 'patrimonio')
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ('id', 'name')
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