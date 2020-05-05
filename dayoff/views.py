from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.apps import apps
# Create your views here.

class ClientList(TemplateView):
    title = 'Lista klientów'
    template_name= 'clientlist/content.html'
    url = 'lista-kliento55sw/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientlist'] = apps.get_model('dayoff.Client').objects.all()
        context['title'] = self.title
        return context

