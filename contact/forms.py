from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
import re

class ContactForm(forms.ModelForm):
    nome = forms.CharField(
            widget = forms.TextInput(
            attrs = {
                'placeholder': "Nome do equipamento",
            }
            ),
            help_text = "Coloque o nome completo do equipamento e marca",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # self.fields['nome'].widget.attrs.update({
        #     'placeholder': "Nome do equipamento",
        #     }
        # )

        # self.nome = forms.CharField(
        #     help_text = "Coloque o nome completo do equipamento e marca",
        # )

        self.fields['lab_usado'].widget.attrs.update({
            'placeholder': "Nome da disciplina",
        })

        self.fields['patrimonio'].widget.attrs.update({
            'placeholder': "Número do patrimônio",
        })


    class Meta:
        model = Contact
        fields = (
            'nome', 'lab_usado','patrimonio',
        )
        # widgets = {
        #     'nome': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Nome do equipamento',
        #         }
        #     ),
        #     'lab_usado' : forms.TextInput(
        #         attrs={
        #             'placeholder': 'Nome da Disciplina',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome')
        lab_usado = cleaned_data.get('lab_usado')

        if nome == lab_usado:
            self.add_error(
                'nome',
                ValidationError(
                'O nome do equipamento e Laboratório são iguais!',
                code = 'invalid'
                )
            )

   
        return super().clean()
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if any(char.isdigit() for char in nome):
            self.add_error(
                'nome',
                ValidationError(
                'Nome inválido, use somente letras',
                code = 'invalid'
                )
            )
        return nome
    
    def clean_patrimonio(self):
        patrimonio = self.cleaned_data.get('patrimonio')

        if len(str(patrimonio)) != 6:
            self.add_error(
                'patrimonio',
                ValidationError(
                'O patrimônio deve conter 6 dígitos',
                code = 'invalid'
                )
            )

        return patrimonio