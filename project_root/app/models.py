from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    content = models.TextField()
    vector = models.BinaryField()

class Similarity(models.Model):
    content1 = models.ForeignKey(Content, related_name='content1', on_delete=models.CASCADE)
    content2 = models.ForeignKey(Content, related_name='content2', on_delete=models.CASCADE)
    similarity = models.FloatField()
