from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory

from .models import Blog
from .forms import BlogForm


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            instance = Blog.objects.get(slug=slug)
            context = {
                'obj' : instance,
            }
            return render(request, self.template_name, context)
        return render(request, "400.html", {})


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user 
        form = BlogForm()
        context = {
        'form' : form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.blog or None, request.FILES or None)
        user = self.request.user
        if form.is_valid():
            myform = form.save(commit=False)
            myform.save()
            return redirect("blog-list")
            context = {
            "form" : myform,
            }
        context = {
        "form" : form,
        }
        return render(request, self.template_name, context)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/edit.html'

    def get(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            obj = Blog.objects.get(slug=slug)
            if obj.user == user:
                form = BlogForm(instance=obj) 
                context = {
                    'object' : obj,
                    'form' : form,
                }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})
        return render(request, "400.html", {})

    def post(self, request, slug=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        user = self.request.user
        if slug is not None:
            obj = Blog.objects.get(slug=slug)
            if obj is not None:
                form = BlogForm(request.blog, request.FILES, instance=obj) 
                if form.is_valid():
                    form.save()
                    return redirect("blog-detail", slug=slug)
                    context = {
                        'object' : obj,
                        'form' : form,
                    }
                context = {
                "object" : obj,
                "form" : form,
                }
                return render(request, self.template_name, context)
            return render(request, "400.html", {})
        return render(request, "400.html", {})
