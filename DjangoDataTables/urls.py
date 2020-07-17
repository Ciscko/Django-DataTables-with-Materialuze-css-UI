
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Articles/', include('MainCrud.urls')),
    path('Blogs/', include('Blogs.urls')),
]
