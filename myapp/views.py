from django.shortcuts import render
from django.http import HttpResponse
from . models import Feature

# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    feature1.Our_service_is_True = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Easy'
    feature2.details = 'Our service is very easy to use'
    feature2.Our_service_is_True = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Reliable'
    feature3.details = 'Our service is very reliable'
    feature3.Our_service_is_True = True

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Cheap'
    feature4.details = 'Our service is cheap to buy'
    feature4.Our_service_is_True = False

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST['text']
    amountOftext = len(text.split())
    return render(request, 'counter.html', {'amount': amountOftext})
