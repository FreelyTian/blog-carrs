from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=20)
    date_pub = models.CharField(max_length=20)
    next_post = models.IntegerField()
    prev_post = models.IntegerField()

    def __str__(self):
        return self.title