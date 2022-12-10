from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from webapp.models import Poll
from webapp.forms import q_form
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q

class Qlist(ListView):
    template_name = "qviewstemp/indexq.html"
    context_object_name = 'poll'
    model = Poll
    ordering = ['-q_date']
    paginate_by = 5

class Qview(DetailView):
    template_name = 'qviewstemp/detailq.html'
    model = Poll

class Qcreate(CreateView):
    template_name = 'qviewstemp/qcreate.html'
    model = Poll
    form_class = q_form
class Qupdate(UpdateView):
    model = Poll
    template_name = 'qviewstemp/qupdate.html'
    form_class = q_form
    context_object_name = 'poll'
class Qdelete(DeleteView):
    model = Poll
    template_name = 'qviewstemp/qdelete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('qindex')


