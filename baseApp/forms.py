from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order
import re
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout,Submit

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=  ['username','email']


def validate_phone_number(value):
    phone_regex = re.compile(r'^\+91?[6789]\d{9}$')
    if not phone_regex.match(value):
        raise ValidationError('Invalid phone number. Please enter a valid phone number.')
    
    
    
class OrderForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)    
        self.helper = FormHelper()    
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Checkout',css_class='btn btn-success'))
    
    class Meta:
        model = Order
        
        fields = ['first_name','last_name','street','city','state','zipcode','phone_number']
        
        def clean_phone_number(self):
            phone_number = self.cleaned_data.get("phone_number")
            validate_phone_number(phone_number)
            return phone_number

    