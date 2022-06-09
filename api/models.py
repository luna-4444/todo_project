from django.db import models

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "List: {}".format(self.name)
