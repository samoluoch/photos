from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category()

    def test_new_category_isinstance_of_category(self):
        self.assertTrue(isinstance(self.new_category, Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location()

    def test_new_location_isinstance_of_location(self):
        self.assertTrue(isinstance(self.new_location, Location))


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(name='nairobi')
        self.new_location.save()

        # Creating a new category and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

        # Creating a new image and saving it

        self.new_image= Image(name = 'Test Image',description = 'This is a random test image',category = 'party', location='nairobi')
        self.new_image.save()

        self.new_image.category.location.add(self.new_category,self.new_location)

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_get_image_today(self):
        image_of_day = Image.image_of_day()
        self.assertTrue(len(image_of_day) > 0)

    def test_get_image_by_date(self):
        '''
        Test to confirm that we are getting images according to a given date
        '''
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        image_by_date = Image.days_image(date)
        self.assertTrue(len(image_by_date) == 0)





# #
# class Image(models.Model):
#     '''
#     This is image class model
#     '''
#     image = models.ImageField(upload_to='image/', null=True)
#     name = models.CharField(max_length =60)
#     description = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category)
#     location = models.ForeignKey(Location, null=True)
#
#     def save_image(self):
#         self.save()
#
#     @classmethod
#     def todays_image(cls):
#         today = dt.date.today()
#         image = cls.objects.filter(pub_date__date=today)
#         return image
#
#     @classmethod
#     def search_by_category(cls, search_term):
#         # cat = category.objects.get(name=search_term)
#         image = cls.objects.filter(category__name__icontains=search_term)
#         return image
#
#     @classmethod
#     def search_by_location(cls, search_term):
#         image = cls.objects.filter(location__name__icontains=search_term)
#         return image
#
#     @classmethod
#     def days_image(cls, date):
#         image = cls.objects.filter(pub_date__date=date)
#         return image