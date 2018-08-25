=======
Contact
=======

Simple web app for a contact form.

Developed using python 3.7 and django 2.1

Quick start
-----------

#. Add "contact" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'contact',
    ]

#. Run `python manage.py migrate` to create the contact model.

#. Add following to urls.py::

    from contact.views import index as contact

    urlpatterns = [
    path('contact/', contact),
    ...
    ]

#. Start the development server and visit http://127.0.0.1:8000/contact/
   to see contact form and create submission.

#. Visit http://127.0.0.1:8000/admin/ to manage contact submissions
   (you'll need the Admin app enabled).

#. (OPTIONAL) Email configuration::

    # in settings.py
    # EMAIL
    EMAIL_BACKEND = 'EMAIL_BACKEND'
    EMAIL_HOST_USER = 'EMAIL_HOST_USER'
    # OPTIONALLY use mailgun.com to send emails
    MAILGUN_ACCESS_KEY = 'MAILGUN_ACCESS_KEY'
    MAILGUN_SERVER_NAME = 'MAILGUN_SERVER_NAME'
    FORM_OWNER_EMAIL = 'FORM_OWNER_EMAIL'
    # Set to True to enable email feature
    EMAIL_CONFIGURED = False

