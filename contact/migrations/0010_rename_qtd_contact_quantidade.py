# Generated by Django 4.2.3 on 2023-08-03 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_rename_quantidade_contact_qtd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='qtd',
            new_name='quantidade',
        ),
    ]
