from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from webapp.models import Choice, Poll
from webapp.forms import c_form
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q



class c_create(CreateView):
    template_name = 'cviewtemp/c_create.html'
    model = Choice
    form_class = c_form

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detailq', kwargs={'pk': self.object.poll.pk})

class c_update(UpdateView):
    template_name = 'cviewtemp/c_update.html'
    form_class = c_form
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('detailq', kwargs={'pk': self.object.poll.pk})

class c_delete(DeleteView):
    template_name = 'cviewtemp/c_delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('detailq', kwargs={'pk': self.object.poll.pk })
