from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    SUCCESS_MESSAGE = "Thank you for reaching out." \
                      " We will be in touch as soon as possible."

    class Meta:
        model = Contact
        fields = "__all__"

    # error_css_class = "error"
    # required_css_class = "required"

    name = forms.CharField(
        required=True, max_length=50, widget=forms.TextInput(
            attrs={
                "placeholder": "Name", "maxlength": "30",
                "class": "w3-third w3-input w3-border", "type": "text"
            }
        )
    )

    email = forms.EmailField(
        required=True, max_length=50, widget=forms.TextInput(
            attrs={
                "placeholder": "Email", "maxlength": "50",
                "class": "w3-third w3-input w3-border", "type": "text"
            }
        )
    )

    phone = forms.CharField(
        required=False, max_length=30, widget=forms.TextInput(
            attrs={
                "placeholder": "Phone", "maxlength": "50",
                "class": "w3-third w3-input w3-border", "type": "text"
            }
        )
    )

    message = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                "placeholder": "Message", "maxlength": "1000",
                "class": "w3-input w3-border", "type": "text"
            }
        )
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
