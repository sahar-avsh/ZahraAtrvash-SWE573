from django import forms

from categorytags.models import Skill, Interest, OfferTag

class SkillForm(forms.ModelForm):
  skill_name = forms.CharField(required=False)
  skill_name_remove = forms.CharField(required=False)
  class Meta:
    model = Skill
    exclude = [
      'name'
    ]

  def save(self, commit=True):
    skill = super().save(commit=False)
    skill.name = self.cleaned_data['skill_name'].title()
    if commit:
        skill.save()
    return skill

class InterestForm(forms.ModelForm):
  interest_name = forms.CharField(required=False)
  interest_name_remove = forms.CharField(required=False)
  class Meta:
    model = Interest
    exclude = [
      'name'
    ]

  def save(self, commit=True):
    interest = super().save(commit=False)
    interest.name = self.cleaned_data['interest_name'].title()
    if commit:
        interest.save()
    return interest

class OfferTagForm(forms.ModelForm):
  offer_tag_name = forms.CharField(required=False)
  class Meta:
    model = OfferTag
    exclude = [
      'name'
    ]

  def save(self, commit=True):
    offertag = super().save(commit=False)
    offertag.name = self.cleaned_data['offer_tag_name'].title()
    if commit:
        offertag.save()
    return offertag