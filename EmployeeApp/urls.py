from django.urls import path
from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('departements/', views.departementApi),
    path('departements/<int:id>', views.departementApi),
    path('employees/', views.employeeApi),
    path('employees/<int:id>', views.employeeApi),
    path('employees/savefile/', views.saveFile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
