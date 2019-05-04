from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher


class DelLoadView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            LoadTeacher.objects.get(id=self.kwargs['load_id']).delete()
            return HttpResponseRedirect(reverse('archive'))
        except:
            return render(request, "index.html")
