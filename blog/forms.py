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
            'category': forms.Select(choices=(
                ('', 'Select Category'),
                ('Mountains', 'Mountains'),
                ('Coasts', 'Coasts'),
                ('Lakes', 'Lakes'),
                ('Forests', 'Forests'),
            )),
            'destination': forms.TextInput(attrs={'placeholder': 'Destination'}),
            'description': forms.Textarea(attrs={'placeholder': 'Share a brief description of your experience'}),
        }  

    def clean_category(self):
        category = self.cleaned_data.get('category')
        valid_choices = [choice[0] for choice in self.Meta.widgets['category'].choices]
        if category == 'Select Category':
            raise forms.ValidationError("Please select a valid category.")
        elif category not in valid_choices:
            raise forms.ValidationError("Invalid category selected.")
        return category  




class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        model = Comment
        fields = ('body',)   
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Enter Comment'}),
        }