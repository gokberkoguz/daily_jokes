# Generated by Django 4.1 on 2022-09-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0003_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
