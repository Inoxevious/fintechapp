from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AccountUser , Country, UserClass
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    date_birth = forms.DateField(help_text='Required. Format: YYYY-NN-DD')

    # role = forms.ChoiceField(
    #     choices=[(x.id,x.name) for x in UserClass.objects.all()]
    #      )

    # def save(self, commit=True):
    #   instance = super().save(commit=False)
    #   role = self.cleaned_data['role']
    #   instance.role = UserClass.objects.get(pk=role)
    #   instance.save(commit)
    #   return instance
        
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'date_birth',  'email', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-signUpForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'SignUp'))

class UserClassForm(forms.Form):
    country = forms.CharField(max_length=30, required=False, help_text='Optional.')
    role = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Mate:
        model = AccountUser
        fields = ('country', 'user_class',)
    
    def __init__(self, *args, **kwargs):
        super(DelegationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-delegationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Continue'))


class DelegationForm(forms.Form):
    country = forms.CharField(max_length=30, required=False, help_text='Optional.')
    role = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Mate:
        model = AccountUser
        fields = ('country', 'role',)
    
    def __init__(self, *args, **kwargs):
        super(DelegationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-delegationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Continue'))