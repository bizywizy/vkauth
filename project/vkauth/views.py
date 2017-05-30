from django.shortcuts import render

from social_django.utils import psa


@psa('social:complete')
def register_by_access_token(request, backend):
    token = request.GET.get('access_token')

    return render('complete.html', context={'token': token})
