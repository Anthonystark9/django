# Generated by Django 3.2.9 on 2021-11-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211118_1526'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='architect_table',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='architect_table',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='architect_table',
            name='password',
        ),
    ]