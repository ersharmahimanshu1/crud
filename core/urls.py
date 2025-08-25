from django.urls import path
from .views import home, add_emp

urlpatterns = [
  path('', home.as_view(), name='home'),
  path('add-emp/', add_emp.as_view(), name='add-emp')

]