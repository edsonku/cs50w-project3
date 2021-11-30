# Generated by Django 3.2.9 on 2021-11-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211125_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.CharField(max_length=50, verbose_name='Tipo de pizza')),
                ('stilo', models.CharField(max_length=50, verbose_name='Estilo')),
                ('size', models.CharField(max_length=75, verbose_name='Tamaño')),
                ('price', models.FloatField(verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.DeleteModel(
            name='Types',
        ),
        migrations.AlterField(
            model_name='dinner',
            name='price',
            field=models.FloatField(verbose_name='Preciodinner'),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='size',
            field=models.CharField(max_length=75, verbose_name='Tamañodinner'),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.FloatField(verbose_name='Preciosub'),
        ),
        migrations.AlterField(
            model_name='salads',
            name='price',
            field=models.FloatField(verbose_name='Preciosub'),
        ),
        migrations.AlterField(
            model_name='subs',
            name='price',
            field=models.FloatField(verbose_name='Preciosub'),
        ),
        migrations.AlterField(
            model_name='subs',
            name='size',
            field=models.CharField(max_length=75, verbose_name='Tamañosub'),
        ),
        migrations.AlterField(
            model_name='topings',
            name='topings',
            field=models.CharField(max_length=50, verbose_name='Tipo_topping'),
        ),
    ]
