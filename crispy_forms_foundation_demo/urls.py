"""
Urls for "crispy form foundation" demo
"""
from django.conf.urls import url, patterns
from django.views.generic.base import TemplateView

from .views import F5IndexView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="crispy_demo/index.html"), name='crispy-demo-index'),
    #url(r'^f3/$', F3IndexView.as_view(), name='crispy-demo-f3-index'),
    url(r'^foundation-5/$', F5IndexView.as_view(), name='crispy-demo-f5-index'),
    url(r'^success/$', TemplateView.as_view(template_name="crispy_demo/success.html"), name='crispy-demo-success'),
)
