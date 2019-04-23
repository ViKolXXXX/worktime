from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher


class ReportView(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            load = LoadTeacher.objects.get(id=self.kwargs['load_id'])
            context = {"load": load}
            return render(request, "report.html", context)
        except:
            return render(request, "index.html")
