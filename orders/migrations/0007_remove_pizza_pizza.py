# Generated by Django 3.2.9 on 2021-11-30 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_detallepasta_detallepizza_ordenes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='pizza',
        ),
    ]
