from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

class UserSignUpForm(UserCreationForm):
    email =forms.EmailField(validators=[validators.validate_email])
    min_length =2
    max_length =30
    name_regex='\A[a-zA-Z]+\Z'
    regex_msg='Name should only contain letters'
    
    message_lt_min = f"shoul have at least {min_length} characters"
    message_ht_max= f"should have at most {max_length} characters"
    first_name=forms.CharField(validators=[validators.MinLengthValidator(min_length, message_lt_min),
    validators.MaxLengthValidator(max_length, message_ht_max), validators.RegexValidator(name_regex,regex_msg)])
    last_name=forms.CharField(validators=[validators.MinLengthValidator(min_length, message_lt_min),
    (max_length,message_ht_max),validators.RegexValidator(name_regex,regex_msg)])
    
    
class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]