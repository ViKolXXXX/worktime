import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher


class GetReport1View(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=Bulletin_.docx'

            return response
        except:
            return render(request, "index.html")
