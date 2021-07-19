# Form for User Complainant Action - Screen 1
from django import forms
from .models import UserComplainScreen1


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = UserComplainScreen1
        fields = ('image', 'name', 'phone')


# Form for User Complainant Action - Screen 3
from django import forms
from .models import UserComplainScreen3


class FeedbackForm(forms.ModelForm):
    feedbacks = (('Very Bad', 'Very Bad'), ('Not Satisfied', 'Not Satisfied'), ('Satisfied', 'Satisfied'), ('Very Good', 'Very Good'))
    feedback = forms.ChoiceField(choices=feedbacks, widget=forms.RadioSelect, required=False)

    class Meta:
        model = UserComplainScreen3
        fields = "__all__"



# Form for User Complainant Action - Screen 4

from django import forms
from .models import UserComplainScreen4


class MessageForm(forms.ModelForm):
    """Form for the message model"""

    class Meta:
        model = UserComplainScreen4
        fields = ('message', )



# Form for Shelter Manager - Screen 2
from django import forms
from .models import RegisterShelterScreen2Model


class RegisterShelterScreen2Form(forms.ModelForm):
    option = (('Yes', 'Yes'), ('No', 'No'))
    hand_pump = forms.ChoiceField(choices=option, widget=forms.RadioSelect, required=False)
    space_keeping_fodder = forms.ChoiceField(choices=option, widget=forms.RadioSelect, required=False)
    space_green_fodder = forms.ChoiceField(choices=option, widget=forms.RadioSelect, required=False)
    dump_area = forms.ChoiceField(choices=option, widget=forms.RadioSelect, required=False)
    electricity = forms.ChoiceField(choices=option, widget=forms.RadioSelect, required=False)

    class Meta:
        model = RegisterShelterScreen2Model
        fields = '__all__'




# Form for Shelter Manager - Screen 3
from django import forms
from .models import RegisterShelterScreen3Model


class FacilitiesForm(forms.ModelForm):
    powers = (('Invertor', 'Invertor'), ('Solar Plant', 'Solar Plant'), ('Global Gas', 'Global Gas'), ('Generator', 'Generator'))
    power_backup = forms.MultipleChoiceField(choices=powers, widget=forms.CheckboxSelectMultiple, required=False)
    incomes = (('Milk Sell', 'Milk Sell'), ('Cow Dung Sell', 'Cow Dung Sell'), ('Compost Sell', 'Compost Sell'),
               ('Urine Sell', 'Urine Sell'), ('By Products', 'By Products'))
    source_of_income = forms.MultipleChoiceField(choices=incomes, widget=forms.CheckboxSelectMultiple, required=False)
    periods = (('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Yearly'))
    veterinary_doctor_visit = forms.ChoiceField(choices=periods, required=False)
    name = forms.CharField(max_length=100, required=False)
    phone = forms.IntegerField()
    option = (('yes', 'yes'), ('no', 'no'))
    availability_of_First_aid = forms.ChoiceField(choices=option, widget=forms.RadioSelect, required=False)

    class Meta:
        model = RegisterShelterScreen3Model
        fields = "__all__"
        labels = {

            "power_backup": "Power Backup",
            "source_of_income": "Source of income",
            "veterinary_doctor_visit": "Visit to Doctor",
            "name": "Name",
            "phone": "Contact No.",
            "availability_of_First_aid": "First-Aid Available?",

        }





# Form for Shelter Manager - Screen 4
from django import forms
from .models import RegisterShelterScreen4Model


class Screen4Form(forms.ModelForm):
    product_details = forms.CharField(max_length=100, required=False)

    class Meta:
        model = RegisterShelterScreen4Model
        fields = '__all__'

