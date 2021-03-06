from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# # Create your models here.
class Post(models.Model):
    # pass
    title = models.CharField(max_length=100, default="")
    image_path = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    code = models.CharField(max_length=1000, default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


