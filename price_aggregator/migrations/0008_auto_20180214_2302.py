# Generated by Django 2.0.2 on 2018-02-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_aggregator', '0007_auto_20180214_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='cache',
            field=models.IntegerField(default=300),
        ),
    ]