from django.shortcuts import render
from . import forms
from booking_site.models import Apartment
from django.db.models import Min

# def index(request):
#     if request.method == 'POST':
#         form = forms.SubscribeForm(request.POST)
#         if form.is_valid():
            
#             print(form.cleaned_data['name'])
#             print(form.cleaned_data['email'])
            
#             form.save(commit=True)
            
#             return render(request, 'booking_site/index.html', {'form': forms.SubscribeForm(), 'success': True})
#     else:
#         form = forms.SubscribeForm()
        
#     return render(request,'booking_site/index.html', context={'form':forms.SubscribeForm(),'success':False})


def index(request):
    apartments = Apartment.objects.all()
    apartments_from = Apartment.objects.all().aggregate(Min('price'))
    print(apartments_from)
    if request.method == 'POST':
        form = forms.SearchAvailabilityForm(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data['check_in'])
            print(form.cleaned_data['check_out'])
            print(form.cleaned_data['adults'])
            print(form.cleaned_data['kids'])
            
            # form.save(commit=True)
            
            return render(request, 'booking_site/index.html', {'form': forms.SearchAvailabilityForm(), 'success': True,'apartments_from':apartments_from})
    else:
        form = forms.SearchAvailabilityForm()
        
    return render(request,'booking_site/index.html', context={'form':forms.SearchAvailabilityForm(),'success':False, 'apartments_from':apartments_from})






def booking(request):
    
    apartments = Apartment.objects.all()
    context = {'apartments':apartments}
    
    return render(request,'booking_site/booking.html', context)

