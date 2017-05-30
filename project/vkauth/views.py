from django.shortcuts import render
import vk


def index_view(request):
    context = {}
    if request.user.is_authenticated:
        social = request.user.social_auth.get(provider='vk-oauth2')
        token = social.extra_data.get('access_token')
        session = vk.Session(access_token=token)
        vkapi = vk.API(session)
        friends = vkapi.friends.get(order='random', count=5,
                                    fields=['domain', 'first_name', 'last_name'])
        context.update({'friends': friends})
    return render(request, 'index.html', context=context)
