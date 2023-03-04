from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    size = models.CharField(max_length=30)
    producer = models.ForeignKey('Producer', on_delete=models.PROTECT, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    cost = models.IntegerField()
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

class Producer(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    country = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name