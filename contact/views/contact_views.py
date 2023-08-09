from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
            .order_by('-id')
    
    paginator = Paginator(contacts, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(
        request, 
        'global/index.html',
        context
        )

def search (request):

    search_value = request.GET.get('q', "").strip()

    if search_value == "":
        return redirect('index')
    

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(Q(name__icontains=search_value) |
                Q(lab_used__icontains=search_value) | 
                Q(patrimonio__icontains=search_value))\
            .order_by('-id')
    
    paginator = Paginator(contacts, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 

    context = {
        'page_obj': page_obj
    }
    return render(
        request, 
        'global/index.html',
        context
        )
   
def equipamento(request, contact_id):


    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f'{single_contact.name} - '

    context = {
        'contact': single_contact,
        'site_title' : site_title
    }
    return render(
        request, 
        'global/equipamento.html',
        context
        )
    