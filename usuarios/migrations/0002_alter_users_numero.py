# Generated by Django 5.0.6 on 2024-06-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]