# Generated by Django 4.2.3 on 2023-08-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_rename_created_data_contact_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='lab_used',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='quantidade',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
