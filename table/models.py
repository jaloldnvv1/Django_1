from django.db import models

class Task(models.Model):
    day = models.CharField(max_length=20)
    task = models.TextField()

    def __str__(self):
        return f"{self.task}"