from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory

from blog.models import Blog

class HomeView(View):
    template_name = 'home.html'

    def get(self, request, slug=None, *args, **kwargs):
        instance = Blog.objects.all()
        context = {
            'obj' : instance,
        }
        return render(request, self.template_name, context)
