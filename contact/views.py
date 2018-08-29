import logging
import json

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm


# Get an instance of a logger
logger = logging.getLogger(__name__)

try:
    EMAIL_CONFIGURED = settings.EMAIL_CONFIGURED
except AttributeError as e:
    logger.warning(
        'WARNING: emails will not be sent after form completion. Set '
        'EMAIL_CONFIGURED to false in settings.py to disable this warning.'
    )
    EMAIL_CONFIGURED = False


def email_form_content(name, email, phone, message):
    """Email the profile with the contact information"""
    template = get_template('contact/contact_template.txt')
    context = {
        'contact_name': name,
        'contact_email': email,
        'contact_phone': phone,
        'contact_message': message,
    }
    content = template.render(context)

    email = EmailMessage(
        subject=f'New contact form submission from {name}',
        body=content,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.FORM_OWNER_EMAIL]
    )
    email.send()


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            contact_phone = request.POST.get('phone', '')
            contact_message = request.POST.get('message', '')

            if EMAIL_CONFIGURED:
                email_form_content(
                    name=contact_name,
                    email=contact_email,
                    phone=contact_phone,
                    message=contact_message
                )

            form.save()
            messages.success(request, form.SUCCESS_MESSAGE)
        else:
            messages.error(
                request,
                [
                    (k, v[0]['message']) for k, v
                    in json.loads(form.errors.as_json()).items()
                ]
            )

    return render(
        request=request,
        template_name='contact/index.html',
        context={'form': form_class},
    )
