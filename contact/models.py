from django.db import models
from django.utils import timezone


# Before
# id(primary_key - autoincrement)
# first_name(string), last_name(string), phone(string)
# email(email), created_data(date), description(text)

# After
# category(forreing_key), show(boolean), owner(foreign_key)
# picture(imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=False) 
    last_name = models.CharField(max_length=100, null=False) 
    phone = models.CharField(max_length=20) 
    email = models.EmailField(max_length=254, blank=True)
    created_data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
