from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    profession = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name