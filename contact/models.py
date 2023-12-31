from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Before
# id(primary_key - autoincrement)
# first_name(string), last_name(string), phone(string)
# email(email), created_data(date), description(text)

# After
# category(forreing_key), show(boolean), owner(foreign_key)
# picture(imagem)

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    nome = models.CharField(max_length=100, null=False) 
    quantidade = models.IntegerField(null=False)
    lab_usado = models.CharField(max_length=100, null=False)
    patrimonio = models.IntegerField(null=True)  
    created_date = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)
    categoria = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        blank=True, null=True
        )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
        )


    def __str__(self) -> str:
        return f'{self.nome}'
