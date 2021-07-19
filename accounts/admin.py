from django.contrib import admin

# complain screen 1
from .models import UserComplainScreen1

admin.site.register(UserComplainScreen1)


# complain screen 3
from .models import UserComplainScreen3

admin.site.register(UserComplainScreen3)


# complain screen 4
from .models import UserComplainScreen4

admin.site.register(UserComplainScreen4)


# Shelter Registration screen 2
from .models import RegisterShelterScreen2Model

admin.site.register(RegisterShelterScreen2Model)


# Shelter Registration screen 3
from .models import RegisterShelterScreen3Model

admin.site.register(RegisterShelterScreen3Model)


# Shelter Registration screen 4
from .models import RegisterShelterScreen4Model

admin.site.register(RegisterShelterScreen4Model)
