import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","apartment_rental.settings")

import django

django.setup()

### Fake Population Script ###
from random_address import real_random_address
import random
from booking_site.models import Apartment
from faker import Faker
import re


fakegen = Faker()

def random_int(value_1,value_2):
    return random.randint(value_1,value_2)
    

def populate_apartments(N=5):
    for _ in range(N):
        
        random_address = real_random_address()
        coordinates = random_address["coordinates"]
        lat = float(coordinates["lat"])
        lng = float(coordinates["lng"])
        contact_person = fakegen.name()
        phone = fakegen.basic_phone_number()
        
        
        extra_text  = fakegen.text(max_nb_chars=300)
        rules = fakegen.text(max_nb_chars=300)
        
        
        
        fake_email = fakegen.email()
        
        apartment = Apartment.objects.get_or_create(street_address = random_address["address1"],
                                                    postal_code = random_address["postalCode"],
                                                    city = random_address["city"],
                                                    state = random_address["state"],
                                                    lat = lat,
                                                    lng = lng,
                                                    email=fake_email,
                                                    phone = phone,
                                                    contact_person=contact_person,
                                                    country="US",
                                                    max_people=random_int(1,5),
                                                    bathrooms=random_int(1,2),
                                                    bedrooms=random_int(1,5),
                                                    check_in = "3PM",
                                                    check_out = "12PM",
                                                    shower=random_int(0,1),
                                                    wifi=random_int(0,1),
                                                    tv=random_int(0,1),
                                                    kitchen=random_int(0,1),
                                                    heating=random_int(0,1),
                                                    accessible=random_int(0,1),
                                                    extra_info=extra_text,
                                                    rules=rules)[0]
        
        
if __name__ == '__main__':
    print("Populating Script")
    populate_apartments(20)
    print("Populating Complete")
    
