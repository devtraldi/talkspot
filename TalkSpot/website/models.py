from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.TextField()
    character = models.CharField(max_length=100)

    def __str__(self):
        return f'"{self.text}" - {self.character}'