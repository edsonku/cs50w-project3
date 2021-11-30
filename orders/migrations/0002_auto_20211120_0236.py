# Generated by Django 3.2.9 on 2021-11-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner', models.CharField(max_length=50, verbose_name='Platillo')),
                ('size', models.CharField(max_length=75, verbose_name='Tamaño')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta', models.CharField(max_length=50, verbose_name='pasta')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salads', models.CharField(max_length=50, verbose_name='Tipo de ensalada')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs', models.CharField(max_length=50, verbose_name='Tipo de Sub')),
                ('size', models.CharField(max_length=75, verbose_name='Tamaño')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Topings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topings', models.CharField(max_length=50, verbose_name='Tipo de pizza')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.CharField(max_length=50, verbose_name='Tipo de pizza')),
                ('size', models.CharField(max_length=75, verbose_name='Tamaño')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]