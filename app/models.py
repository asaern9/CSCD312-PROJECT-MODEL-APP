from django.db import models

# Create your models here.

class Picture(models.Model):
    picture = models.ImageField(upload_to='test_pics/', null=False)

    def __str__(self):
        return self.picture.name