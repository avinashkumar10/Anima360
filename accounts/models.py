from django.db import models

# Create your models here.

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


# User Complainant Action - Screen 1
from django.db import models


class UserComplainScreen1(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")

    def __str__(self):
        return 'Image: {} Name: {} Phone: {}'.format(self.image, self.name, self.phone)


# User Complainant Action - Screen 3

from django.db import models


class UserComplainScreen3(models.Model):
    feedbacks = (('Very Bad', 'Very Bad'), ('Not Satisfied', 'Not Satisfied'), ('Satisfied', 'Satisfied'),
                 ('Very Good', 'Very Good'))
    feedback = models.CharField(max_length=100, choices=feedbacks)

    def __str__(self):
        return self.feedback


# User Complainant Action - Screen 4
from django.db import models


class UserComplainScreen4(models.Model):
    message = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.message


# Shelter Manager - Screen 2
from django.db import models


class RegisterShelterScreen2Model(models.Model):
    shaded_area = models.FloatField()
    non_shaded_area = models.FloatField()
    option = (('Yes', 'Yes'), ('No', 'No'))
    hand_pump = models.CharField(max_length=10, choices=option)
    fodder = models.FloatField()
    space_keeping_fodder = models.CharField(max_length=10, choices=option)
    space_green_fodder = models.CharField(max_length=10, choices=option)
    dump_area = models.CharField(max_length=10, choices=option)
    electricity = models.CharField(max_length=10, choices=option, default="")
    no_of_fans = models.FloatField()
    no_of_light = models.FloatField()

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.shaded_area, self.non_shaded_area, self.hand_pump,
                                                      self.fodder, self.space_keeping_fodder, self.space_green_fodder,
                                                      self.dump_area, self.electricity, self.no_of_fans,
                                                      self.no_of_light)




# Shelter Manager - Screen 3
from django.db import models
from multiselectfield import MultiSelectField

class RegisterShelterScreen3Model(models.Model):
    powers = (('Invertor', 'Invertor'), ('Solar Plant', 'Solar Plant'), ('Global Gas', 'Global Gas'), ('Generator', 'Generator'))
    power_backup = MultiSelectField(choices=powers)
    incomes = (('Milk Sell', 'Milk Sell'), ('Cow Dung Sell', 'Cow Dung Sell'), ('Compost Sell', 'Compost Sell'),
               ('Urine Sell', 'Urine Sell'), ('By Products', 'By Products'))
    source_of_income = MultiSelectField(max_length=100, choices=incomes)
    periods = (('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Yearly'))
    veterinary_doctor_visit = MultiSelectField(max_length=100, choices=periods)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    option = (('yes', 'yes'), ('no', 'no'))
    availability_of_First_aid = models.CharField(max_length=100, default="", choices=option)

    def __str__(self):
        return 'Power Backup: {} ; Source of Income: {} ; Doctors Visit: {} ; Name: {} ; Contact No.: {} ; First-aid Available?: {}'.format(self.power_backup, self.source_of_income, self.veterinary_doctor_visit, self.name, self.phone, self.availability_of_First_aid)





# Shelter Manager - Screen 4
from django.db import models
from datetime import datetime, date


class RegisterShelterScreen4Model(models.Model):
    product_details = models.CharField(max_length=200, default="")
    purchase_date = models.DateField('Purchase Date (mm/dd/yyyy)', auto_now_add=False, auto_now=False, blank=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    product_quantity = models.IntegerField()
    amount = models.FloatField()
    upload_bill = models.ImageField(upload_to='images')

    def __str__(self):
        return 'Product Details:{} | Purchase Date: {} | Time Stamp: {} | Product Quantity: {} | Amount: {} | Upload bill: {}'.format(self.product_details, self.purchase_date, self.timestamp,
                                          self.product_quantity, self.amount, self.upload_bill)
