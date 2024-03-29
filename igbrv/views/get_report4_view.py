import datetime
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher

from docxtpl import DocxTemplate


class GetReport4View(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            load = LoadTeacher.objects.get(id=self.kwargs['load_id'])
            path2template = os.path.join("igbrv", "docx_templates", "report4.docx")
            doc = DocxTemplate(path2template)
            context = {'g1': load.g1,
                       'g2': load.g2,
                       
                       'sum_g': load.sum_g
                       }
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=4.docx'
            doc.render(context)
            doc.save(response)

            return response
        except:
            return render(request, "index.html")
