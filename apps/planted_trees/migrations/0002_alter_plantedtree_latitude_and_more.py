# Generated by Django 5.0.6 on 2024-06-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planted_trees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantedtree',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
        migrations.AlterField(
            model_name='plantedtree',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=15),
        ),
    ]
