from django.test import TestCase

from .contact_forms import *
from contact.forms import ContactForm, SUCCESS_MESSAGE


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
        self.assertEqual(
            form.is_valid(), False, msg='Expected is_valid() to be False'
        )
        self.assertEqual(
            form.is_bound, True, msg='Expected is_bound to be True'
        )
        self.assertEqual(
            form.errors,
            {
                'email': [
                    u'Ensure this value has at most 50 characters (it has 60).'
                ]
            },
            msg='Error message does not match expected output.'
        )
        self.assertEqual(form.data, too_long_email_data, msg='')
        self.assertNotEqual(form.data, {}, msg='')

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
