
from django.shortcuts import render
from django.views.generic import TemplateView


class CalculationView(TemplateView):

    def get(self, request, *args, **kwargs):
       return render(request, "calculation.html")
