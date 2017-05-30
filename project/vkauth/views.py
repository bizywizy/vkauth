from django.shortcuts import render

from social_django.utils import psa


@psa('social:complete')
def user(request):
    token = request.GET.get('access_token')

    return render('complete.html', context={'token': token})
