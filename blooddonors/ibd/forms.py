from django import  forms
from .models import  Donor , DonorHistory



class  DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        labels = {
            'donor_name'  : '*Full Name',
            'blood_group' : '*Blood Group',
            'donor_std'   : '* STD Code',
            'donor_zip'   : 'Postal Pincode',
            'donor_phone' : '* Mobile Number',
            'donor_email' : '* Email Address'

        }
        fields = "__all__"
