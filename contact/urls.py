from django.urls import path
from contact.views import *

urlpatterns = [
    path('', contact_views.index, name='index'),
    path('<int:contact_id>/', contact_views.equipamento, name='equipamento'),
]