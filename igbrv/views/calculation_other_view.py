from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class CalculationOtherView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "calculation-other.html")

    def post(self, request):
        return render(request, "calculation-other.html")
