# Generated by Django 2.0.2 on 2018-02-14 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_aggregator', '0008_auto_20180214_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='supported_providers',
        ),
    ]
