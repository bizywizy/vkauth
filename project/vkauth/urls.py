from django.conf.urls import url

from django.views.generic import TemplateView

from .views import user

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='login'),
    url(r'user/(?P<backend>[^/]+)/$', user, name='user')
]
