from django.urls import path
from contact.views import *

urlpatterns = [
    path('', contact_views.index, name='index'),
]