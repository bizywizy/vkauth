from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import vk

@login_required
def user(request):
    social = request.user.social_auth.get(provider='vk-oauth2')
    token = social.extra_data.get('access_token')
    vkapi = vk.API(access_token=token)
    friends = vkapi.friends.get(order='random', count=5)
    return render(request, 'complete.html', context={'friends': friends})
