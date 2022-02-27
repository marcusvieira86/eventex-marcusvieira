from django.test import TestCase
from eventex.subscriptions.forms import SubscritionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscritionForm()


    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))
