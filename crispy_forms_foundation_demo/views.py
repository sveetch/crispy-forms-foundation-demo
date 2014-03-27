# -*- coding: utf-8 -*-
"""
Views
"""
from django import template
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

from .forms import Foundation5Form

class F5IndexView(FormView):
    template_name = 'crispy_demo/foundation-5.html'
    form_class = Foundation5Form
    
    def get_success_url(self):
        return reverse('crispy-demo-success', args=[])
