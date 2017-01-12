
from django import  forms
from .models import Question
from django.forms import ModelForm


class NameForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=200)
    cc_myself = forms.BooleanField(required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class AuthorForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        labels = {
            'question_text': ('Writer'),
        }
        help_texts = {
            'question_text': ('Some useful help text.'),
        }
        error_messages = {
            'question_text': {
                'max_length': ("This writer's name is too long."),
            },
        }


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


