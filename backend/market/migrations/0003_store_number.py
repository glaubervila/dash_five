# Generated by Django 2.1.2 on 2018-10-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='number',
            field=models.PositiveIntegerField(default=0, verbose_name='Number'),
        ),
    ]
