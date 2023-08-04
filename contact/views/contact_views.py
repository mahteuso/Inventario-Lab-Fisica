from django.shortcuts import render
from contact.models import Contact


def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
            .order_by('-id')[:10]

    context = {
        'contacts': contacts
    }
    return render(
        request, 
        'global/index.html',
        context
        )
def equipamento(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact': single_contact
    }
    return render(
        request, 
        'global/equipamento.html',
        context
        )
    