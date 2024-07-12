from django import forms
from django_recaptcha.fields import ReCaptchaField, ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your Name', 
                                max_length=100,
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder' : 'Your Name',
                                        'type' : 'text',
                                        'name' : 'name',
                                        'class': 'form-control',
                                        'id' : 'name',
                                        }
                                    ),
                                required=True)
    your_email = forms.EmailField(label='Your Email',
                                  widget=forms.TextInput(
                                    attrs={
                                        'placeholder' : 'Your Email',
                                        'type' : 'email',
                                        'name' : 'email',
                                        'class': 'form-control',
                                        'id' : 'email',
                                        }
                                    ),
                                  required=True)
    subject = forms.CharField(max_length=200,
                              widget=forms.TextInput(
                                    attrs={
                                        'placeholder' : 'Subject',
                                        'type' : 'text',
                                        'name' : 'subject',
                                        'class': 'form-control',
                                        'id' : 'subject',
                                        }
                                    ),
                              required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={
                                'placeholder' : 'Message',
                                'type' : 'text',
                                'name' : 'message',
                                'class': 'form-control',
                                'rows' : '5',}),
                              required=True)
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-callback': 'enableFormSubmit',
            }
        )
    )