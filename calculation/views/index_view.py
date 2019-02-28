from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")
