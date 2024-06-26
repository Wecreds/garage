from django.db import models

class Accessory(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"

class Category(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"