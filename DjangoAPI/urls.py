from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('EmployeeApp.urls')),
    path('admin/', admin.site.urls),
]
