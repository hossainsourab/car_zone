from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def cars(request):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars': paged_cars
    }
    return render(request, 'cars/cars.html', context=data)


def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car
    }
    return render(request, 'cars/car_details.html', context=data)
