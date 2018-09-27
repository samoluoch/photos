from django.db import models


# Create your models here.

class Category(models.Model):
    '''
    This is the cetgories class
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Image(models.Model):
    '''
    This is image class model
    '''
    image = models.ImageField(upload_to='image/', null=True)
    name = models.CharField(max_length =60)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    # location = models.ForeignKey(Location)

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls, search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image

    @classmethod
    def search_by_location(cls, search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image






