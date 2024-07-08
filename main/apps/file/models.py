from django.db import models
from django.contrib.auth.models import User
from ..common import BaseModel


class FileGroup(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class File(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    group = models.ForeignKey(FileGroup, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
