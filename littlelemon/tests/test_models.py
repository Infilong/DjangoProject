from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse


class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(
            id=1, title="IceCream", price=80, inventory=100)
        expected_values = {
            'id': 1,
            'title': 'IceCream',
            'price': 80,
            'inventory': 100,
            '_state': item._state,
        }

        self.assertDictEqual(item.__dict__, expected_values,
                             "Properties should be equal")