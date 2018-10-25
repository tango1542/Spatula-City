from django.db import models
from django.urls import reverse             #The reverse module is for reverse direction URLs (Getting a URL from the name of a view)

class Category(models.Model):               #All of the fields for the category model
    name=models.CharField(max_length=150, db_index=True)
    slug=models.SlugField(max_length=150, unique=True, db_index=True)       #The slug field is for simplyfying the ugly URL name
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):             #This method is creating friendly URLs
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):        #All of the fields for the product model
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):         #This method is creating friendly URLs
        return reverse('shop:product_detail', args=[self.id, self.slug])



