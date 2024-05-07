from django import forms
from .models import RegisterNgo 
from .models import UserProfile   # Import the RegisterNgo model

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisterNgo
        fields = '__all__'  # Include all fields for validation

    def clean_email(self):
        # Custom email validation (optional)
        email = self.cleaned_data['email']
        # Your email validation logic here (e.g., check for @ and .)
        return email

    def clean_contact(self):
        # Custom contact number validation (optional)
        contact = self.cleaned_data['contact']
        # Your contact number validation logic here (e.g., check length or format)
        return contact
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website', 'phone_number']  # Customize these fields as needed