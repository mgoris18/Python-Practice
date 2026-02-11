import unittest

def get_discount(price):
    if price is None:
        return None
    return price * 0.9


def test_price_is_none(self):
    self.assertIsNone(get_discount(None))