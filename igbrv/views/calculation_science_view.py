from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class CalculationScienceView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "calculation-science.html")

    def post(self, request):
        return render(request, "calculation-science.html")
