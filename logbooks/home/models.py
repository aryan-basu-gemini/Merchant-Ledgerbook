from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    amount=models.IntegerField()
    def _str_(self):
        return self.name