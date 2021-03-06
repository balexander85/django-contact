import logging

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

from .models import Contact, ContactAdmins


logger = logging.getLogger(__name__)

SUCCESS_MESSAGE = "Thank you for reaching out. We will be in touch as soon as possible."

try:
    EMAIL_CONFIGURED = settings.EMAIL_CONFIGURED
except AttributeError as e:
    logger.warning(
        "WARNING: emails will not be sent after form completion. Set "
        "EMAIL_CONFIGURED to false in settings.py to disable this warning."
    )
    EMAIL_CONFIGURED = False


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "maxlength": "30",
                "class": "w3-third w3-input w3-border",
                "type": "text",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "maxlength": "50",
                "class": "w3-third w3-input w3-border",
                "type": "text",
            }
        ),
    )

    phone = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone",
                "maxlength": "50",
                "class": "w3-third w3-input w3-border",
                "type": "text",
            }
        ),
    )

    message = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Message",
                "maxlength": "1000",
                "class": "w3-input w3-border",
                "type": "text",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = ""
        self.fields["email"].label = ""
        self.fields["phone"].label = ""
        self.fields["message"].label = ""

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")
        return cleaned_data

    def send_email(self):
        """Email the profile with the contact information"""
        contact_name = self.cleaned_data.get("name")
        if EMAIL_CONFIGURED:
            contact_admin_list = [x.email for x in ContactAdmins.objects.all()]
            template = get_template("contact/contact_template.txt")
            context = {
                "contact_name": contact_name,
                "contact_email": self.cleaned_data.get("email"),
                "contact_phone": self.cleaned_data.get("phone"),
                "contact_message": self.cleaned_data.get("message"),
            }
            content = template.render(context)

            logger.info(f'Email Sent to {", ".join(contact_admin_list)}')

            send_mail(
                subject=f"New form submission from {contact_name}",
                message=content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=contact_admin_list,
            )
