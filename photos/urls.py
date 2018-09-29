from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^images/',views.welcome,name = 'welcome'),
    url(r'^$',views.all_images,name = 'image'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_image,name = 'pastImages'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name = 'specificImage'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)