# Generated by Django 4.2.2 on 2023-09-02 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sold',
        ),
    ]
