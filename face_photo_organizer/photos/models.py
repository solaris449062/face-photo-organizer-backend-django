from django.db import models
from django.contrib.auth.models import User
    
class Photo(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    total_faces = models.IntegerField()
    tagged_faces = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(max_length=500, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Identity(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Face(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name