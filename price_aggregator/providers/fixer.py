import logging
from decimal import Decimal

import requests


logger = logging.getLogger(__name__)


class Fixer(object):
    """
    https://fixer.io
    """
    @staticmethod
    def get_prices(currencies):
        logger.info('Fixer: Getting prices')

        r = requests.get(
            url='https://api.fixer.io/latest?base=USD'
        )

        if r.status_code != requests.codes.ok:
            return None, 'bad status code: {}'.format(r.status_code)

        try:
            data = r.json()
        except ValueError:
            return None, 'no json: {}'.format(r.text)

        rates = data.get('rates')

        if not rates:
            return None, 'no rates found in data: {}'.format(data)

        search_codes = [coin.code.upper() for coin in currencies]
        output = {}

        for currency_code in rates:
            if currency_code in search_codes:
                for coin in currencies:
                    if coin.code.upper() == currency_code:
                        output[coin] = Decimal(1 / rates.get(currency_code))

        return output, 'success'