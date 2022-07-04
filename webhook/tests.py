from django.test import TestCase
from . models import *


class TestModels(TestCase):
    def setUp(self):
        list1 = TodoList.objects.create(
            title="Todo 1", description="Something to do.")
        list2 = TodoList.objects.create(
            title="Todo 2", description="Something more to do.")
        list1.save()
        list2.save()

    def test_todo_list_model(self):
        todo_list = TodoList.objects.get(title="Todo 1")
        self.assertEqual(todo_list.title, "Todo 1")
        self.assertEqual(todo_list.description, "Something to do.")
