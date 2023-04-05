from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.name

