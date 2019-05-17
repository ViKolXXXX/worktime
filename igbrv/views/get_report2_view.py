import datetime
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher

from docxtpl import DocxTemplate


class GetReport2View(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            load = LoadTeacher.objects.get(id=self.kwargs['load_id'])
            path2template = os.path.join("igbrv", "docx_templates", "report2.docx")
            doc = DocxTemplate(path2template)
            context = {'z': load.z,
                       'z2': load.z2,
                       'z4': load.z4,
                       'z6': load.z6,
                       'z8': load.z8,
                       'z10': load.z10,
                       'z12': load.z12,
                       'z13': load.z13,
                       'z14': load.z14,
                       'z15': load.z15,
                       'z16': load.z16,
                       'z18': load.z18,
                       'z19': load.z19,
                       'z20': load.z20,
                       'z21': load.z21,
                       'z23': load.z23,
                       'z25': load.z25,
                       'z27': load.z27,
                       'z29': load.z29,
                       'z31': load.z31,
                       'z33': load.z33,
                       'z36': load.z36,
                       'z38': load.z38,

                       'sum_z': load.sum_z
                       }
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=2.docx'
            doc.render(context)
            doc.save(response)

            return response
        except:
            return render(request, "index.html")
