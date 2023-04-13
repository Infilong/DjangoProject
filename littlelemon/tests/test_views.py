from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model()()
        self.user.username = 'admin'
        self.user.password = 'littlelemon59354366423!'
        self.user.save()
        # Create some test instances of the Menu model
        Menu.objects.create(id=1, title="Ice Cream", price=3.99, inventory=50)
        Menu.objects.create(id=2, title="Hamburger", price=8.99, inventory=100)
        Menu.objects.create(id=3, title="French Fries",
                            price=2.99, inventory=75)

    def test_getall(self):
        url = reverse('menu')
        self.client.force_login(self.user)
        response = self.client.get(url)
        
        # response.data will be a dictionary with keys like 'count', 'next', 'previous' for pagination, 
        # and 'results' which contains the actual list of menus.
        menus = response.data['results']
        
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(menus, serializer.data)
