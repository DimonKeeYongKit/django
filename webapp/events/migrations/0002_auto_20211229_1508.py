# Generated by Django 3.2.10 on 2021-12-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclubuser',
            name='first_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myclubuser',
            name='last_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
