# Generated by Django 3.2.7 on 2021-09-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login_id',
        ),
    ]
