from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all().order_by('pk')
        context['projects'] = projects
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
