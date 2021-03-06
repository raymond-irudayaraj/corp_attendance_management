# Generated by Django 3.2.7 on 2021-09-14 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('total_logins', models.IntegerField(default=1, null=True)),
                ('total_logouts', models.IntegerField(default=0, null=True)),
                ('attendance_status', models.CharField(max_length=9, null=True)),
                ('working_window', models.IntegerField(default=0, null=True)),
                ('active_window', models.IntegerField(default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField(default=False, null=True)),
                ('time', models.TimeField(auto_now=True)),
                ('active_time', models.IntegerField(default=0, null=True)),
                ('logid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.attendance')),
            ],
        ),
    ]
