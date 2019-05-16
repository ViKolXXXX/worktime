import datetime
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher

from docxtpl import DocxTemplate


class GetReport1View(TemplateView):
    def get(self, request, *args, **kwargs):
        # try:
            load = LoadTeacher.objects.get(id=self.kwargs['load_id'])
            path2template = os.path.join("igbrv", "docx_templates", "report1.docx")
            doc = DocxTemplate(path2template)
            context = {'y1': load.y1,
                       'y3': load.y3,
                       'y5': load.y5,
                       'y9': load.y9,
                       'y11': load.y11,
                       'y13': load.y13,
                       'y15': load.y15,
                       'y17': load.y17,
                       'y19': load.y19,
                       'y21': load.y21,
                       'y23': load.y23,
                       'y27': load.y27,
                       'y25': load.y25,
                       'y29': load.y29,
                       'y31': load.y31,
                       'y32': load.y32,
                       'y34': load.y34,
                       'y36': load.y36,
                       'y38': load.y38,
                       'y39': load.y39,
                       'y41': load.y41,
                       'y43': load.y43,
                       'y45': load.y45,
                       'y47': load.y47,
                       'y49': load.y49,
                       'y50': load.y50,
                       'y51': load.y51,
                       'y53': load.y53,
                       'y532': load.y532,
                       'y55': load.y55,
                       'y57': load.y57,
                       'y59': load.y59,
                       'y61': load.y61,
                       'y63': load.y63,
                       'y65': load.y65,
                       'y67': load.y67,
                       'y71': load.y71,
                       'y731': load.y731,
                       'y732': load.y732,
                       'y733': load.y733,
                       'y734': load.y734,
                       'y75': load.y75,
                       'y76': load.y76,
                       'y77': load.y77,
                       'y79': load.y79,
                       'y80': load.y80,
                       'y82': load.y82,
                       'y84': load.y84,
                       'y86': load.y86,
                       'y88': load.y88,
                       'y90': load.y90,
                       'y92': load.y92,
                       'y94': load.y94,
                       'y96': load.y96,
                       'y98': load.y98,
                       'y99': load.y99,
                       'y100': load.y100,
                       'y102': load.y102,
                       'sum_y': load.sum_y
                       }
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=1.docx'
            doc.render(context)
            doc.save(response)

            return response
        # except:
        #     return render(request, "index.html")
