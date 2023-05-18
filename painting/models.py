from django.db import models
from django.conf import settings

# Create your models here.
class Painting(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    upload_date = models.DateTimeField(auto_now_add=True)

class UserLikePainting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    