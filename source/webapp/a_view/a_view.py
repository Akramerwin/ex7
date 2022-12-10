from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
from webapp.models import Choice, Poll, Answer
from webapp.forms import answer_form
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.db.models import Q


class a_index(TemplateView):
    template_name = 'aviewtemp/a_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = get_object_or_404(Poll, pk=kwargs['pk'])
        form = answer_form(self.request.POST)
        context["form"] = form
        return context