from __future__ import unicode_literals
from django.db import models


class Contact(models.Model):
    """Basic information to collect from a contact form."""
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=False)
    contact_date = models.DateTimeField('contact_date', auto_now_add=True)

    def __str__(self):
        return self.name
