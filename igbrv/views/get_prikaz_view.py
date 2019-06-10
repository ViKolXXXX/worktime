import datetime
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher

from docxtpl import DocxTemplate


class GetPrikazView(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            path2prikaz = os.path.join("igbrv", "docx_templates", "prikaz.docx")
            doc = DocxTemplate(path2prikaz)
            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=prikaz.docx'
           
            doc.save(response)

            return response
        except:
            return render(request, "index.html")
