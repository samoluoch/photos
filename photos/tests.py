from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.Party = Category(name='Party').save()

    def test_new_category_isinstance_of_category(self):
        self.assertTrue(isinstance(self.Party, Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.Nairobi = Location('Nairobi')

    def test_new_location_isinstance_of_location(self):
        self.assertTrue(isinstance(self.Nairobi, Location))


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(name='Nairobi')
        self.new_location.save()

        # Creating a new category and saving it
        self.new_category = Category(name = 'Party')
        self.new_category.save()

        # Creating a new image and saving it

        self.new_image= Image(name = 'Test Image',description = 'This is a random test image',category = 'Party', location='nairobi')
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


    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
