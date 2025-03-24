from django import forms  # type:ignore
from django.contrib.auth.forms import UserCreationForm  # type:ignore
from django.contrib.auth.forms import User  # type:ignore
from .models import Record




    
class signUpform(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    first_name=forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}), help_text='')
    last_name=forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}), help_text='')
  

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(signUpform, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User name'
        self.fields['username'].label=''
        self.fields['username'].help_text=''

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text=''

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''

       


class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name= forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Second name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    phone_number =forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}))
    address= forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    city= forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    state= forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}))
    zipcode= forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'})) 
 
    class Meta:
        model = Record
        exclude=("user",) # this wil add all the fields of above
        