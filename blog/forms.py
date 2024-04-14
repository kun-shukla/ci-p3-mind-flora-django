from django import forms
from .models import UserRecommendedDestination, Comment

class ShareDiscoveryForm(forms.ModelForm):
    """
    Form class for users to suggest a recommended travel destination 
    """
    class Meta:
        model = UserRecommendedDestination
        fields = ('full_Name','email','category','destination','description')
        widgets = {
            'full_Name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'category': forms.Select(attrs={'placeholder': 'Select Category'}, choices=(
                ('', 'Select Category'),
                ('Mountains', 'Mountains'),
                ('Coasts', 'Coasts'),
                ('Lakes', 'Lakes'),
                ('Forests', 'Forests'),
            )),
            'destination': forms.TextInput(attrs={'placeholder': 'Destination'}),
            'description': forms.Textarea(attrs={'placeholder': 'Share a brief description of your experience'}),
        }    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)   
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Enter Comment'}),
        }