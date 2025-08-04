from django.db import models

# Create your models here.

class Product(models.Model):
    SIZES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', '2XL'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.CharField(max_length=3, choices=SIZES, default='M')
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
