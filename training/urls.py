from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('aswathi',include('aswathi.urls')),
    path('admin/', admin.site.urls),
    path('Aysha/',include('Aysha.urls')),
]