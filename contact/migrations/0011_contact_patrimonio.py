# Generated by Django 4.2.3 on 2023-08-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_rename_qtd_contact_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='patrimonio',
            field=models.IntegerField(null=True),
        ),
    ]
