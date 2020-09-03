
from django.db import models


class Cartoon(models.Model):
    name = models.CharField(max_length=60)
    showday = models.CharField(max_length=60)
    def __str__(self):
        return self.name

