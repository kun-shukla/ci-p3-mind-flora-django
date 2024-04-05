from django import forms
from .models import UserRecommendedDestination

class ShareDiscoveryForm(forms.ModelForm):
    """
    Form class for users to suggest a recommended travel destination 
    """
    class Meta:
        model = UserRecommendedDestination
        fields = ('name','email','category','dest_title','description')