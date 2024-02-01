from django.db import models

# Create your models here.
class Demo2app(models.Model):

    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    de=models.TextField()


    def __str__(self):
        return self.name