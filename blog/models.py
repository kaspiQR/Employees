from django.db import models
from django.urls import reverse


class Employee(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})

    def __str__(self):
        return self.name

