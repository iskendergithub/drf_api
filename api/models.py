from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
