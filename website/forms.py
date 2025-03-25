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
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)  # Make sure this excludes only user, not phone