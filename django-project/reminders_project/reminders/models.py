from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=300)

    def __str__(self) -> str:
        return f"{self.title}, {self.description}"

