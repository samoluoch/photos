from django.db import models
import datetime as dt


# Create your models here.

class Category(models.Model):
    '''
    This is the cetegories class
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    '''
    This is the location class
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
    location = models.ForeignKey(Location, null=True)

    def save_image(self):
        self.save()

    @classmethod
    def todays_image(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date=today)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        # cat = category.objects.get(name=search_term)
        image = cls.objects.filter(category__name__icontains=search_term)
        return image

    @classmethod
    def search_by_location(cls, search_term):
        image = cls.objects.filter(location__name__icontains=search_term)
        return image

    @classmethod
    def days_image(cls, date):
        image = cls.objects.filter(pub_date__date=date)
        return image

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images






