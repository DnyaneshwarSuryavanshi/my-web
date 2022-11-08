from django.db import models


# Create your models here.
class registration(models.Model):
    name = models.CharField(max_length=11)
    roll_no = models.CharField(max_length=10)
    contact_no = models.IntegerField()
    # text_field = models.TextField()
    url_field = models.URLField()


# def __str__(self):
#     return self.name
