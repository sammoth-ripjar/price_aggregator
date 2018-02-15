import logging
from statistics import mean, stdev, variance

from django.core.management import BaseCommand
from django.utils.timezone import now

from price_aggregator import providers
from price_aggregator.models import Currency, AggregatedPrice, ProviderFailure, \
    ProviderResponse

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for currency in Currency.objects.all():

            prices = []

            # get the distinct providers from the provider responses
            valid_responses = ProviderResponse.objects.filter(
                currency=currency,
                update_by__gte=now()
            )

            prices = [response.value for response in valid_responses]

            if not prices:
                logger.warning('Got no valid responses for {}'.format(currency))
                continue

            # save an aggregated price
            agg_price = mean(prices)

            logger.info('Got aggregated price of {} for {}'.format(agg_price, currency))

            AggregatedPrice.objects.create(
                currency=currency,
                aggregated_price=agg_price,
                providers=len(prices),
                standard_deviation=stdev(prices, agg_price) if len(prices) > 1 else 0,
                variance=variance(prices, agg_price) if len(prices) > 1 else 0,
            )






