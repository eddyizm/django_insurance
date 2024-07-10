# quote/views.py
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django import forms as django_forms
from . import forms, models
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

# need to import views in the urls.py of quote

# Create your views here.


class Customer_CreateView(CreateView):
    model = models.Customer
    fields = [
        "first_name",
        "last_name",
        "address",
        "telephone_number",
        "zip_code",
        "email_address",
        "date_of_birth",
        "home_ownership",
    ]
    template_name = "customer.html"

    def get_success_url(self):
        return f"/quote/customer/{self.object.pk}"


class Customer_UpdateView(UpdateView):
    model = models.Customer
    fields = [
        "first_name",
        "last_name",
        "address",
        "zip_code",
        "telephone_number",
        "email_address",
        "date_of_birth",
        "home_ownership",
    ]
    template_name_suffix = "_update_form"
    template_name = "customer.html"

    def get_success_url(self):
        return f"/quote/customer/{self.object.pk}"

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = "My Company"
        context['description'] = "We provide the best services."
        return context

class AboutPageView(TemplateView): 
    template_name = "about.html"

    