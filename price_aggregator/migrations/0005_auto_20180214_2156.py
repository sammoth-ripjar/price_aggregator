# Generated by Django 2.0.2 on 2018-02-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_aggregator', '0004_auto_20180214_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aggregatedprice',
            name='number_of_providers',
        ),
        migrations.AddField(
            model_name='aggregatedprice',
            name='providers',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=25),
        ),
    ]
