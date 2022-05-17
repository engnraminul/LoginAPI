from datetime import datetime
from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    image = models.ImageField(upload_to='agent')
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name