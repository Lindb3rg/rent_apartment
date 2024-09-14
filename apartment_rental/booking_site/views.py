from django.shortcuts import render
from . import forms
from booking_site.models import Apartment

def index(request):
    if request.method == 'POST':
        form = forms.SubscribeForm(request.POST)
        if form.is_valid():
            
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            
            form.save(commit=True)
            
            return render(request, 'booking_site/index.html', {'form': forms.SubscribeForm(), 'success': True})
    else:
        form = forms.SubscribeForm()
        
    return render(request,'booking_site/index.html', context={'form':forms.SubscribeForm(),'success':False})







def booking(request):
    
    apartments = Apartment.objects.all()
    context = {'apartments':apartments}
    
    return render(request,'booking_site/booking.html', context)

