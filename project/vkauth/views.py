from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def user(request):
    user = User.objects.get(pk=request.user.pk)
    social = user.social_auth.get(provider='vk-oauth2')
    return render(request, 'complete.html', context={'social': social})
