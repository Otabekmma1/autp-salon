from django.urls import path
from .views import cars, brand_car, car_detail

urlpatterns = [
    path('', cars, name='home'),
    path('brand/<int:brand_id>/', brand_car, name='brand_id'),
    path('detail/<int:id>/', car_detail, name='car_detail'),

]