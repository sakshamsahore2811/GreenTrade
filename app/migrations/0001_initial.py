# Generated by Django 4.2.2 on 2023-09-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=50)),
                ('sold', models.CharField(default=False, max_length=50)),
            ],
        ),
    ]
