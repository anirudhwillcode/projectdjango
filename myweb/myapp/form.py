from django.forms import ModelForm
from myapp.models import Contact

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        




class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','subject','message']