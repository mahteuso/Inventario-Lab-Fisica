# Generated by Django 4.2.3 on 2023-08-03 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_rename_first_name_contact_lab_used_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='quantidade',
            new_name='qtd',
        ),
    ]
