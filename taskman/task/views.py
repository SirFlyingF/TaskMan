from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Task, STATUS_CHOICES
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/home.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"statuses": STATUS_CHOICES, 'cols':12//len(STATUS_CHOICES)})
        return context
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    template_name = 'task/detail.html'

    def test_func(self):
        ''' the test that UserPassesTestMixin calls'''
        task = self.get_object()
        uzr = self.request.user
        if task.user == uzr or uzr.is_superuser:
            return True
        return False


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['description', 'status']
    
    def test_func(self):
        ''' the test that UserPassesTestMixin calls'''
        task = self.get_object()
        uzr = self.request.user
        if task.user == uzr or uzr.is_superuser:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/task/home/'

    def test_func(self):
        ''' the test that UserPassesTestMixin calls'''
        task = self.get_object()
        uzr = self.request.user
        if task.user == uzr or uzr.is_superuser:
            return True
        return False


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = '/task/home/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)