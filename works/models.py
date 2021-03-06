from django.db import models

# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=254, default='')
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    media = models.CharField(max_length=254, default='')
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name