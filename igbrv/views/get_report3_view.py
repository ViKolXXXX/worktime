import datetime
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher

from docxtpl import DocxTemplate


class GetReport3View(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            load = LoadTeacher.objects.get(id=self.kwargs['load_id'])
            path2template = os.path.join("igbrv", "docx_templates", "report3.docx")
            doc = DocxTemplate(path2template)
            context = {'f1': load.f1,
                       'f2': load.f2,
                       'f3': load.f3,
                       'f4': load.f4,
                       'f5': load.f5,
                       'f6': load.f6,                      

                       'sum_f': load.sum_f
                       }
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=3.docx'
            doc.render(context)
            doc.save(response)

            return response
        except:
            return render(request, "index.html")
