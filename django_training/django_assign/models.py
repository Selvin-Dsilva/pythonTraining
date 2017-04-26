from django.db import models

# Create your models here.
class Cust(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    addrline1 = models.TextField()
    addrline2 = models.TextField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    email=models.EmailField()
    area_code=models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name