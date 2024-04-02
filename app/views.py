from django.shortcuts import render, redirect
from .models import Car, Brand, Colour


def cars(request):
    cars = Car.objects.all()
    three_car = Car.objects.all()[0:2]
    brands = Brand.objects.all()
    ctx = {
        'cars': cars,
        'brands': brands,
        'three_cars': three_car

    }
    return render(request, 'base.html', ctx)

def brand_car(request, brand_id):
    cars = Car.objects.filter(brand_id=brand_id)
    brands = Brand.objects.all()
    ctx = {
        'cars': cars,
        'brands': brands
    }
    return render(request, 'blog/brands.html', ctx)


def car_detail(request, id):
    car = Car.objects.filter(id=id)
    brands = Brand.objects.all()

    context = {
        'car': car,
        'model': car.model,
        'brands': brands,
        'name': brands.name
    }
    return render(request, 'blog/detail.html', context=context)
