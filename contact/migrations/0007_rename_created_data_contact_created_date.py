# Generated by Django 4.2.3 on 2023-07-18 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_contact_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_data',
            new_name='created_date',
        ),
    ]
