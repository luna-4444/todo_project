from django.test import TestCase
from ..models import TodoList


# Write a test for models
class TestModels(TestCase):
    def setUp(self):
        TodoList.objects.create(title="Casper", description="Bull Dog")
        TodoList.objects.create(title="Muffin", description="Gradane")

    def test_puppy_breed(self):
        puppy_casper = TodoList.objects.get(title="Casper")
        puppy_muffin = TodoList.objects.get(title="Muffin")
        self.assertEqual(puppy_casper.title, "Casper")
        self.assertEqual(puppy_muffin.title, "Muffin")
