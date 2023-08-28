from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({
            'placeholder': "Nome do equipamento",
        })
        self.fields['lab_usado'].widget.attrs.update({
            'placeholder': "Nome da disciplina",
        })

    class Meta:
        model = Contact
        fields = (
            'nome', 'quantidade', 'lab_usado','patrimonio',
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
        #cleaned_data = self.cleaned_data

        self.add_error(
            'nome',
            ValidationError(
            'Mensagem de erro',
            code='invalid'
            )
        )

        self.add_error(
            'nome',
            ValidationError(
            'Mensagem de erro',
            code='invalid'
            )
        )

        return super().clean()