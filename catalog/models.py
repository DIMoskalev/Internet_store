from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        pass


class Category(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        pass
