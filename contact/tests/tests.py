import requests

from django.test import TestCase

from .contact_forms import *
from contact.forms import ContactForm


SUCCESS_MESSAGE = "Thank you for reaching out. " \
                  "We will be in touch as soon as possible."


class ContactFormTests(TestCase):

    def test_contact_form_with_valid_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(good_data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.SUCCESS_MESSAGE, SUCCESS_MESSAGE)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(form.errors, {})
        self.assertEqual(form.data, good_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_valid_data_no_phone(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(good_data_no_phone)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.SUCCESS_MESSAGE, SUCCESS_MESSAGE)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(form.errors, {})
        self.assertEqual(form.data, good_data_no_phone)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_lauren_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(lauren_data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.SUCCESS_MESSAGE, SUCCESS_MESSAGE)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(form.errors, {})
        self.assertEqual(form.data, lauren_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_brian_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(brian_data)
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(form.SUCCESS_MESSAGE, SUCCESS_MESSAGE)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(form.errors, {})
        self.assertEqual(form.data, brian_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_empty_name_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(empty_name_data)
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(
            form.errors, {'name': [u'This field is required.']}
        )
        self.assertEqual(form.data, empty_name_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_too_long_name_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(too_long_name_data)
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(
            form.errors,
            {
                'name': [
                    u'Ensure this value has at most 50 characters (it has 58).'
                ]
            }
        )
        self.assertEqual(form.data, too_long_name_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_no_name_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(no_name_data)
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(
            form.errors, {'name': [u'This field is required.']}
        )
        self.assertEqual(form.data, no_name_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_empty_email_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(empty_email_data)
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(
            form.errors, {'email': [u'This field is required.']}
        )
        self.assertEqual(form.data, empty_email_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_too_long_email_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(too_long_email_data)
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(
            form.errors,
            {
                'email': [
                    u'Ensure this value has at most 50 characters (it has 60).'
                ]
            }
        )
        self.assertEqual(form.data, too_long_email_data)
        self.assertNotEqual(form.data, {})

    def test_contact_form_with_no_email_data(self):
        """
        Verify valid data returns correct response.
        """
        form = ContactForm(no_email_data)
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.is_bound, True)
        self.assertEqual(
            form.errors, {'email': [u'This field is required.']}
        )
        self.assertEqual(form.data, no_email_data)
        self.assertNotEqual(form.data, {})


class ContactRequests:

    local_url = 'http://localhost:8000/contact/'
    production_url = ''

    def __init__(self, prod_env=False):
        self.session = requests.session()
        self.url = self.production_url if prod_env else self.local_url
        self.csrftoken = self._csrftoken
        self.response = self.session.post(self.url, data=self.form_data)

    @property
    def _csrftoken(self):
        self.session.get(self.url)
        return self.session.cookies.get('csrftoken')

    @property
    def form_data(self):
        return dict(
            name="First Last",
            email="email.address@example.com",
            phone="555-555-5555",
            message="Testing contact form with python request.",
            csrfmiddlewaretoken=self.csrftoken
        )


class TestContactFormRequest(TestCase):

    def test_valid_contact_form_with_requests(self):
        contact = ContactRequests()
        assert contact.response.status_code == 200
