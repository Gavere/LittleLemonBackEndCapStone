# tests/test_models.py
from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu_str_representation(self):
        # Create an instance of the Menu model
        menu_item = Menu.objects.create(Title="Ice Cream", Price=80, Inventory=100)
        
        # Test the __str__() method to check if the representation is correct
        self.assertEqual(str(menu_item), "Ice Cream - $80")
