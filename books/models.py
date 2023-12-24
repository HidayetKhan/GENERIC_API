from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=120)
    auther=models.CharField(max_length=200)
    published_date=models.DateField()

    def __str__(self):
        return self.title