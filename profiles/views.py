from django.core.exceptions import ValidationError
from django.http.response import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import ProfileModelForm
from .models import Profile, ProfileFollowRequest
from offers.models import Offer
from categorytags.models import Skill, Interest

# Create your views here.
def home_view(request, *args, **kwargs):
  qs_offers = Offer.objects.all()
  # get the active user with request.user
  # get following list and list their joined offers
  content = {'offer_list': qs_offers}
  return render(request, 'home.html', content)

def profile_edit_view(request, *args, **kwargs):
  profile = get_object_or_404(Profile, pk=request.user.profile.id)
  if request.method == 'POST':
    form = ProfileModelForm(request.POST, instance=profile)
    if form.is_valid():
      profile = form.save()
      return redirect('profile_look', pk=profile.id)
    print(form.errors)
  else:
    form = ProfileModelForm(instance=profile)
  return render(request, "profiles/forms.html", {'form': form})

def profile_outlook_view(request, pk, *args, **kwargs):
  current_profile = request.user.profile
  current_profile_friend_list = current_profile.friends.all()
  try:
    obj = Profile.objects.get(pk=pk)
    skill_list = obj.skills.all()
    interest_list = obj.interests.all()
    friend_list = obj.friends.all()
  except (Profile.DoesNotExist, ValidationError):
    raise Http404
  return render(request, "profiles/outlook.html", {"object": obj, "user": current_profile,
   "skill_list": skill_list, "interest_list": interest_list, 'friend_list': friend_list, 
   'user_friend_list': current_profile_friend_list})

def profile_notifications_view(request, *args, **kwargs):
  current_profile = request.user.profile
  try:
    friend_requests = ProfileFollowRequest.objects.all().filter(following_profile_id=current_profile)
  except ProfileFollowRequest.DoesNotExist:
    friend_requests = None
  content = {"object_list": friend_requests}
  return render(request, "profiles/notifications.html", content)

def profile_activity_background_view(request, *args, **kwargs):
  obj = request.user.profile
  created_offers = Offer.objects.all().filter(owner=obj)
  joined_offers = obj.accepted_offers.all()
  outstanding_offers = obj.outstanding_offers.all()
  content = {'created_offers': created_offers, 
  'joined_offers': joined_offers,
  'outstanding_offers': outstanding_offers}
  return render(request, "profiles/activity_background.html", content)

""" def profile_api_detail_view(request, pk, *args, **kwargs):
  try:
      obj = Profile.objects.get(pk=pk)
  except (Profile.DoesNotExist, ValidationError):
      return JsonResponse(
          {"Message": "Not found!"}, status=404
      )  # render JSON with HTTP status code of 404
  return JsonResponse({"First name": obj.f_name}) """

def send_follow_request(request, profileID):
  from_profile = request.user.profile
  to_profile = Profile.objects.get(pk=profileID)
  follow_request, created = ProfileFollowRequest.objects.get_or_create(
    profile_id=from_profile, following_profile_id=to_profile
  )
  if created:
    return redirect('home_page')
  else:
    return redirect('home_page')

def unfollow(request, profileID):
    from_profile = request.user.profile
    to_profile = Profile.objects.get(pk=profileID)
    from_profile.friends.remove(to_profile)
    to_profile.friends.remove(from_profile)
    return redirect('home_page')

def accept_follow_request(request, follow_request_id):
  follow_request = ProfileFollowRequest.objects.get(id=follow_request_id)
  if follow_request.following_profile_id == request.user.profile:
    follow_request.profile_id.friends.add(follow_request.following_profile_id)
    follow_request.following_profile_id.friends.add(follow_request.profile_id)
    follow_request.delete()
    return redirect('home_page')
  else:
    return redirect('home_page')

def decline_follow_request(request, follow_request_id):
  follow_request = ProfileFollowRequest.objects.get(id=follow_request_id)
  if follow_request.following_profile_id == request.user:
    follow_request.delete()
    return redirect('home_page')
  else:
    return redirect('home_page')

def profile_friends_view(request, *args, **kwargs):
  current_profile = request.user.profile
  friend_list = current_profile.friends.all()
  content = {"object_list": friend_list}
  return render(request, "profiles/friends.html", content)