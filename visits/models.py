from django.db import models

from blog.models import Employee


class Visit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    visited = models.BooleanField(default=True)
    time_visit_start = models.TimeField()
    time_visit_end = models.TimeField()
    reason = models.CharField(max_length=255)
