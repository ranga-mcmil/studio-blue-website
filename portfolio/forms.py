from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):

    name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Your Name"
        }
    ))

    subject = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Subject"
        }
    ))

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': "Your Message"
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'name': 'email',
            'placeholder': "Your Email"
        }
    ))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        message = cl_data.get('message')
        name = cl_data.get('name')
        email = cl_data.get('email')
        subject = cl_data.get('subject')

        return message, name, email, subject

    def send(self):

        message, name, email, subject = self.get_info()

        send_mail(
            subject=f"WEBSITE QUERY - {subject}",
            message=f'{message} - /n from /n {name} - {email}' ,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
