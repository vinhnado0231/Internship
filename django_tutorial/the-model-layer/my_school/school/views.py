from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,DetailView

from .models import Student, Class


class IndexView(ListView):
    model = Class
    template_name = 'school/index.html'
    context_object_name = 'class_list'

    def get_queryset1(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Class.objects.filter(name__icontains=search_query)
        return Class.objects.all()


class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student_detail.html'


class ClassDetailView(DetailView):
    model = Class
    template_name = 'school/class_detail.html'
