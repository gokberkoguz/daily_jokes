# Generated by Django 4.1 on 2022-09-24 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joke',
            old_name='is_user',
            new_name='is_used',
        ),
    ]