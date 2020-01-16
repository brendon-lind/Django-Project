from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        proj = Project.objects.all().order_by('-title')
        context['projectos'] = proj

        context['people'] = ['Nic', 'Brendon', 'Bailey']
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
