from django.db import models
from django.utils import timezone

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, default='title')
    text = models.TextField(default='text')
    is_completed = models.BooleanField(default=False)
    is_permanent = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(default=0)
    task_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.title