from django import forms
from .models import Listing, PropertyGallary

class Add_Listing(forms.ModelForm):
    class Meta:
        model   =   Listing
        exclude =   ['agent', 'is_published', 'slug', 'list_date', 'start_date',]
        fields  =   "__all__"

class PropertyGallary(forms.ModelForm):
    class Meta:
        model   =   PropertyGallary
        fields  =   ("image",)



    # def __init__(self, *args, **kwargs):
    #     super(Add_Listing, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'
