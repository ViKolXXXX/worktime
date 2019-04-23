from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher


class ArchiveView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            loads = LoadTeacher.available_requests(request.user)

            context = {"loads": loads}
            return render(request, "archive.html", context)

        except:
            return render(request, "index.html")
