from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user(request):
    return render(request, 'complete.html', context={'items': dir(request.user)})
