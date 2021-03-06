from django import forms
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.models import User

# from mapbox_location_field.forms import LocationField
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis import forms as gis_forms

# from django_starfield import Stars

from profiles.models import OwnerToParticipantReview, Profile, ProfileReview

import datetime

class DateInput(forms.DateInput):
  input_type = 'date'

class ProfileModelForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      'image',
      'f_name',
      'l_name',
      'birthday',
      'occupation',
      'education',
      'description',
      'location',
    ]

    widgets = {
      'birthday': DateInput(),
      'location': GooglePointFieldWidget,
    }

  def clean_f_name(self):
    data = self.cleaned_data.get('f_name')
    if len(data) < 2:
      raise forms.ValidationError('This is not long enough.')
    return data

  def clean_l_name(self):
    data = self.cleaned_data.get('l_name')
    if len(data) < 2:
      raise forms.ValidationError('This is not long enough.')
    return data

  def clean_birthday(self):
    data = self.cleaned_data.get('birthday')
    now = datetime.date.today()
    if data:
      if data > now:
        raise forms.ValidationError('Your birthday cannot be later than now.')
      return data

class ReviewForm(forms.ModelForm):
  CHOICES_RATING = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
  ]

  CHOICES_DONE = [
    (True, 'Approve'),
    (False, 'Decline')
  ]
  rating = forms.ChoiceField(choices=CHOICES_RATING, widget=forms.RadioSelect)
  done = forms.ChoiceField(choices=CHOICES_DONE, widget=forms.RadioSelect)
  # rating = forms.IntegerField()
  class Meta:
    model = ProfileReview
    fields = [
      'text',
    ]

class OwnerToParticipantReviewForm(forms.ModelForm):
  CHOICES_RATING = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
  ] 
  rating = forms.ChoiceField(choices=CHOICES_RATING, widget=forms.RadioSelect)
  class Meta:
    model = OwnerToParticipantReview
    fields = [
      'text'
    ]

class ProfileSearchForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(), required=False)

class CustomSignupForm(SignupForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=30, label='First Name')
  last_name = forms.CharField(max_length=30, label='Last Name')
 
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


    def save(self, commit=True):
      user = super().save(commit=False)

      user.email = self.cleaned_data['email']
      user.first_name = self.cleaned_data['first_name']
      user.last_name = self.cleaned_data['last_name']

      if commit:
          user.save()
      return user

class CustomLoginForm(LoginForm):
  login = forms.EmailField()
  class Meta:
    model = User
    fields = ('login', 'password')


  def login(self, *args, **kwargs):

    # Add your own processing here.

    # You must return the original result.
    return super(CustomLoginForm, self).login(*args, **kwargs)