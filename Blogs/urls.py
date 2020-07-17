from django.urls import path
from .views import Blogs

urlpatterns  = [
    path('', Blogs, name="Blog_list")
]
