from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from django.apps import apps
from django.urls import reverse_lazy, reverse
# Create your views here.

class Dashboard(TemplateView):
    title = 'Panel sterowania'
    template_name = 'dashboard/content.html'
    url = ''

class ClientList(TemplateView):
    title = 'Lista klientów'
    template_name= 'clientlist/content.html'
    url = 'lista-klientow/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientlist'] = apps.get_model('dayoff.Client').objects.all()
        context['title'] = self.title
        return context

class ClientCreate(CreateView):
    model = apps.get_model('dayoff.Client')
    title = 'Dodaj klienta'
    template_name = 'clientcreate/content.html'
    url = 'dodaj-klienta/'
    fields = ['first_name', 'last_name', 'postal_code', 'street', 'city', 'nip']

    def get_success_url(self):
        return reverse('clientlist')


class ClientDelete(DeleteView):
    model = apps.get_model('dayoff.Client')
    url = 'usun-klienta/<pk>'
    template_name = 'clientdelete/content.html'
    success_url = reverse_lazy('clientlist')

class OrderList(TemplateView):
    title = 'Lista zamówień'
    template_name = 'orderlist/content.html'
    url = 'lista-zamowien/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderlist'] = apps.get_model('dayoff.Order').objects.all()
        context['title'] = self.title
        return context


class OrderCreate(CreateView):
    model = apps.get_model('dayoff.Order')
    template_name = 'ordercreate/content.html'
    url = 'dodaj-zamowienie/'
    fields = ['client', 'product', 'price', 'title', 'description', 'begin_date', 'finish_date']

    def get_success_url(self):
        return reverse('orderlist')

class OrderDelete(DeleteView):
    model = apps.get_model('dayoff.Order')
    url = 'usun-zamowienie/<pk>'
    template_name = 'orderdelete/content.html'
    success_url = reverse_lazy('orderlist')
