from django.urls import path
from contact.views import *


urlpatterns = [
    path('', contact_views.index, name='index'),
    path('searc/', contact_views.search, name='search'),

    # equipaments (CRUD)
    path('equipament/create/', create_views.create, name='create'),
    path('equipament/<int:contact_id>/detail/', contact_views.equipamento, name='equipamento'),
   
]