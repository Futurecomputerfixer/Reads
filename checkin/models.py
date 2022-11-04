from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(blank=True, max_length=500)
    author = models.CharField(blank=True, max_length=500)
    checkouts = models.PositiveIntegerField(default=0)
    image = models.TextField(blank=True)
    def __str__(self):
        return f"{self.id}:{self.title}"


class Record(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="records")
    timestamp = models.DateTimeField(auto_now_add=True)
    checkin = models.BooleanField(default=False)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="records")

    def __str__(self):
        return f"{self.id}:{self.user} checked {self.book} at {self.timestamp}"
