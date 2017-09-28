from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def __repr__(self):
        return self.title