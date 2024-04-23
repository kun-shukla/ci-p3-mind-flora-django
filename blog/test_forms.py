from django.test import TestCase
from .forms import CommentForm, ShareDiscoveryForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'yhuhij'})
        self.assertTrue(comment_form.is_valid(),msg="Body content was provided but the form is not valid")
    
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Body content not provided but form is valid")

class TestShareDiscoveryForm(TestCase):

    def test_form_is_valid(self):
        """ Test for valid form fields """
        form = ShareDiscoveryForm({
            'full_Name': 'kunal',
            'email': 'test@test.com',
            'category': 'Mountains',
            'destination': 'xyz',
            'description': 'abc xyz',
        })
        self.assertTrue(form.is_valid(), msg="All field values correctly provided but form is not valid")


    def test_form_is_invalid_when_placeholdertxt_selected_for_category_field(self):
        """ Test for 'Select Category' placeholder selected for category field """
        form = ShareDiscoveryForm({
            'full_Name': 'kunal',
            'email': 'test@test.com',
            'category': 'Select Category',  # This is placeholder text, which is not a valid category option
            'destination': 'xyz',
            'description': 'abc xyz',
        })
        self.assertFalse(form.is_valid(), msg="'Select Category' placeholder text selected in the 'category' field but Form is valid")
    

    def test_form_is_valid_when_a_valid_preset_category_option_is_selected(self):
        """ Test for valid category field"""
        form = ShareDiscoveryForm({
            'full_Name': 'kunal',
            'email': 'test@test.com',
            'category': 'Forests',  # Provide a valid category value
            'destination': 'xyz',
            'description': 'abc xyz',
        })
        self.assertTrue(form.is_valid(), msg="Valid category option provided but forms fails")

 
