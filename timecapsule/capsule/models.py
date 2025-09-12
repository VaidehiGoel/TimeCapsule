from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Capsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    unlock_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional media uploads
    image = models.ImageField(upload_to='capsules/images/', blank=True, null=True)
    video = models.FileField(upload_to='capsules/videos/', blank=True, null=True)
    audio = models.FileField(upload_to='capsules/audio/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
