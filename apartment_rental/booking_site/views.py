from django.shortcuts import render

def index(request):
    return render(request,'booking_site/index.html', context={})

def booking(request):
    return render(request,'booking_site/booking.html', context={})