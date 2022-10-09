from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)

    content = models.TextField(null=True, blank=True)

    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
