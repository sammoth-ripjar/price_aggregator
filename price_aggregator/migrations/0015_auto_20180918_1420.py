# Generated by Django 2.0.2 on 2018-09-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_aggregator', '0014_auto_20180918_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='numarketmaker',
            name='market_target',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=25),
        ),
        migrations.AddField(
            model_name='numarketmaker',
            name='multiplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multiplier', to='price_aggregator.Currency'),
        ),
        migrations.AlterField(
            model_name='numarketmaker',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='price_aggregator.Currency'),
        ),
    ]
