from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


def create(request):
    contacts = Contact.objects\
        .filter(show=True)\
            .order_by('-id')

    context = {
        'contact': contacts
    }
    return render(
        request, 
        'global/create.html',
        context
        )