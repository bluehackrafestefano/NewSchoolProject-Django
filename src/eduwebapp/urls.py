from django.urls import path
from .views import home, about, blog, contact, blogsingle, coursegrid2, coursegrid3, coursegrid4, pricing, teachers

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('blogsingle', blogsingle, name='blogsingle'),
    path('coursegrid2', coursegrid2, name='coursegrid2'),
    path('coursegrid3', coursegrid3, name='coursegrid3'),
    path('coursegrid4', coursegrid4, name='coursegrid4'),
    path('pricing', pricing, name='pricing'),
    path('teachers', teachers, name='teachers'),
]