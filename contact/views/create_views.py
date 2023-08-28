from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm




def create(request):

    if request.method == 'POST':
        print(request.POST)
        context = {
                'form': ContactForm(request.POST)
        }
        return render(
            request, 
            'global/create.html',
            context
            )
    context = {
                'form': ContactForm()
        }
    return render(
        request, 
        'global/create.html',
        context
        ) 