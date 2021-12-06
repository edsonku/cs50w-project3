# Generated by Django 3.2.9 on 2021-12-01 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_pizza_pizza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='stilo',
            new_name='pizza',
        ),
        migrations.CreateModel(
            name='Detallesub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('price', models.FloatField(verbose_name='precio')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='orders.ordenes')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.subs')),
            ],
        ),
        migrations.CreateModel(
            name='Detallesalads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('price', models.FloatField(verbose_name='precio')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salad', to='orders.ordenes')),
                ('salad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.salads')),
            ],
        ),
        migrations.CreateModel(
            name='Detalledinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('price', models.FloatField(verbose_name='precio')),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.dinner')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinner', to='orders.ordenes')),
            ],
        ),
    ]
