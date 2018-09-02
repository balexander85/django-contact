import json

from django.contrib import messages
from django.views.generic import FormView

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    success_url = '/test/'
    template_name = 'contact/index.html'

    def form_valid(self, form):
        form.save()
        form.send_email()
        messages.success(self.request, form.SUCCESS_MESSAGE)
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(
            self.request,
            [
                (k, v[0]['message'])
                for k, v in json.loads(form.errors.as_json()).items()
            ]
        )
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form)
        )
