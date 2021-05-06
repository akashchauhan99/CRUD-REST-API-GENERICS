from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    userName = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.email


class Blog(models.Model):
    blogText = models.CharField(max_length=500)
    blogImg = models.FileField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    pubDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.blogText
