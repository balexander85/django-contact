import json

from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
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
