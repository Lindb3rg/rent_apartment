from django.db import models

class Subscribe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    
class Apartment(models.Model):
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9,decimal_places=6, default=0)
    lng = models.DecimalField(max_digits=9,decimal_places=6, default=0)
    email = models.EmailField()
    max_people = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    bedrooms = models.PositiveSmallIntegerField(default=0)
    check_in = models.CharField(max_length=10)
    check_out = models.CharField(max_length=10)
    shower = models.BooleanField(default=0)
    wifi = models.BooleanField(default=0)
    tv = models.BooleanField(default=0)
    kitchen = models.BooleanField(default=0)
    heating = models.BooleanField(default=0)
    accessible = models.BooleanField(default=0)
    extra_info = models.TextField(max_length=100)
    rules = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}"
    
# class Attachment(models.Model):
#     class AttachmentType(models.TextChoices):
#         PHOTO = "Photo", ("Photo")
#         VIDEO = "Video", ("Video")

#     file = models.ImageField('Attachment', upload_to='attachments/')
#     file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)

#     publication = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name='Apartment Model')

#     class Meta:
#         verbose_name = 'Attachment'
#         verbose_name_plural = 'Attachments'