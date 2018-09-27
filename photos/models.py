from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Category)
    # location = models.ForeignKey(Location)



