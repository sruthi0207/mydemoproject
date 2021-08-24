from django.db import models

# Create your models here.
class Rest(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    flavour = models.TextField()
    img = models.ImageField(upload_to='profile_img/')

    def __str__(self):
        return self.name
