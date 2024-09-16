from django.shortcuts import render
from . import forms
from booking_site.models import Apartment
from django.db.models import Min

#Login Functionality
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    apartments = Apartment.objects.all()
    apartments_from = Apartment.objects.all().aggregate(Min('price'))
    print(apartments_from)
    text = "Hello world!"
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
        
    return render(request,'booking_site/index.html', context={'form':forms.SearchAvailabilityForm(),'success':False, 'apartments_from':apartments_from,'hello':text})



def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            print("**** USER FORM ****")
            print(user_form.cleaned_data['username'])
            print(user_form.cleaned_data['email'])
            print(user_form.cleaned_data['password'])
            print("**** PROFILE FORM ****")
            print(profile_form.cleaned_data['portfolio_site'])
            print(profile_form.cleaned_data['profile_pic'])
            
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
            
            return render(request, 'booking_site/index.html', {'user_form': user_form,'profile_form':profile_form, 'success': True, 'registered':registered})
            
        else:
            print(user_form.errors,profile_form.errors)
                
                
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
            
            
            

    
    return render(request,'booking_site/registration.html', context={'user_form': forms.UserForm(),'profile_form':forms.UserProfileInfoForm(), 'success':False, 'registered':registered})




def booking(request):
    
    apartments = Apartment.objects.all()
    context = {'apartments':apartments}
    
    return render(request,'booking_site/booking.html', context)




def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login credentials applied")
    else:
        return render(request,'booking_site/login.html', {})
            
            

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))