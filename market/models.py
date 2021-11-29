from django.db import models
from django.db.models.base import ModelState


# Create your models here.

class Products(models.Model):
    title = models.CharField("name", max_length=60)
    # prod_image = models.ImageField(upload_to = "market/static/images")
    prod_decription = models.TextField()

    def get_absolute_url(self):
        return f'/self.id'
    

    def __str__(self):
        return self.title
