from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
import uuid


# Create your models here.
class Profile(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(blank=True, upload_to='images/')
  f_name = models.CharField(max_length=50)
  l_name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  birthday = models.DateField(null=True, blank=True)
  occupation = models.CharField(blank=True, max_length=50)

  loc_long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  loc_ltd = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  location = gis_models.PointField(null=True, blank=True, srid=4326, verbose_name='Location')

  class DiplomaReceived(models.TextChoices):
    other = 'Other', _('Other')
    high_school = 'High School Diploma', _('High School Diploma')
    associate = 'Associate Degree', _('Associate Degree')
    undergraduate = 'Undergraduate Degree', _('Undergraduate Degree')
    postgraduate = 'Postgradute Degree', _('Postgraduate Degree')

  education = models.CharField(max_length=50, choices=DiplomaReceived.choices, blank=True)

  description = models.TextField(blank=True)
  credit = models.DecimalField(max_digits=4, decimal_places=2, default=5.00)
  # offers that profile has requested to join
  # outstanding_offers = models.ManyToManyField('offers.Offer', related_name='profiles_outstanding', blank=True)
  # offers that profile has been accepted to join
  accepted_offers = models.ManyToManyField('offers.Offer', related_name='profiles_accepted', blank=True)
  # skills that profile has
  skills = models.ManyToManyField('categorytags.Skill', related_name='profiles', blank=True)
  # interests that profile has
  interests = models.ManyToManyField('categorytags.Interest', related_name='profiles', blank=True)
  # friends
  friends = models.ManyToManyField('Profile', blank=True)

  def __str__(self) -> str:
    return self.f_name + ' ' + self.l_name

class ProfileFollowRequest(models.Model):
  profile_id = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
  following_profile_id = models.ForeignKey('Profile', related_name='followers', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
      return self.profile_id.f_name + ' Follows ' + self.following_profile_id.f_name

class ProfileReview(models.Model):
  review_giver = models.ForeignKey('Profile', related_name='review_receiver', on_delete=models.CASCADE)
  offer = models.ForeignKey('offers.Offer', related_name='about', on_delete=models.CASCADE, null=True)
  done = models.BooleanField(default=True)
  rating = models.IntegerField(default=0)
  text = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
      return self.review_giver.f_name + '->' + self.offer.title + '-' + self.offer.owner.f_name

class OwnerToParticipantReview(models.Model):
  offer = models.ForeignKey('offers.Offer', related_name='offer_owner', on_delete=models.CASCADE)
  participant = models.ForeignKey('Profile', related_name='offer_participant', on_delete=models.CASCADE)
  rating = models.IntegerField(null=True, blank=True)
  text = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
      return self.offer.owner.f_name + '-->' + self.offer.title + '-' + self.participant.f_name

class ProfileJoinOfferRequest(models.Model):
  profile = models.ForeignKey('Profile', related_name='joiner', on_delete=models.CASCADE)
  offer = models.ForeignKey('offers.Offer', related_name='joined_offer', on_delete=models.CASCADE)
  is_accepted = models.BooleanField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
      return self.profile.f_name + ' wants to join ' + self.offer.title