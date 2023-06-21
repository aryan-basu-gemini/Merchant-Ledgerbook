from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    amount=models.IntegerField()
    total=models.IntegerField(default=0)
    phone=models.CharField(default=0,max_length=12)
    primary=models.CharField(default=0,max_length=100)
    def _str_(self):
        return self.name
    
class Product(models.Model):
    primary=models.CharField(default=0,max_length=100)
    amount=models.IntegerField()
    description=models.TextField()
    name=models.CharField(max_length=200)
