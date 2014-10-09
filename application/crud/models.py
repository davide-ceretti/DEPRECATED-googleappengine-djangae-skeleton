from django.db import models


class Item(models.Model):
    value = models.CharField(max_length=255)
