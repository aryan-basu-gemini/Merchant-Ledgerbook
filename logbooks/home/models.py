from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    amount=models.IntegerField()
    total=models.IntegerField(default=0)
    def _str_(self):
        return self.name