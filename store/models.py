from django.db import models
from django.contrib.auth.models import User
from .validators import validate_phone_number

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=200, unique=True,db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

PROVINCES_CHOICES=[
    ('Lower Silesia','Lower Silesia'),
    ('Kuyavia-Pomerania','Kuyavia-Pomerania'),
    ('Lodzkie','Lodzkie'),
    ('Lublin','Lublin'),
    ('Lubusz','Lubusz'),
    ('Lesser Poland','Lesser Poland'),
    ('Masovia','Masovia'),
    ('Subcarpathia','Subcarpathia'),
    ('Pomerania','Pomerania'),
    ('Silesia','Silesia'),
    ('Warmia-Masuria','Warmia-Masuria'),
    ('Greater Poland','Greater Poland'),
    ('West Pomerania','West Pomerania')
]

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    province = models.CharField(max_length=64, choices=PROVINCES_CHOICES, default="Poland")
    phone_number = models.CharField(max_length=9,validators=[validate_phone_number], default="987654321")

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name