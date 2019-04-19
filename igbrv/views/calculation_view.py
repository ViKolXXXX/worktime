from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from igbrv.models import LoadTeacher


class CalculationView(TemplateView):

    def get(self, request, *args, **kwargs):
       return render(request, "calculation.html")

    def post(self, request):
        load = LoadTeacher()

        load.x = request.POST.get('X')

        load.y1 = request.POST.get('Y')*0.5
        load.y3 = request.POST.get('Y2')*0.2
        load.y5 = request.POST.get('Y4')*0.3
        load.y7 = request.POST.get('Y6')*70
        load.y9 = request.POST.get('Y8')*90
        load.y11 = request.POST.get('Y10')*35
        load.y13 = request.POST.get('Y12')*45
        load.y15 = request.POST.get('Y14')*3
        load.y17 = request.POST.get('Y16')*12
        load.y19 = request.POST.get('Y18')*6
        load.y21 = request.POST.get('Y20')*40
        load.y23 = request.POST.get('Y22')*20
        load.y25 = request.POST.get('Y24')*10
        load.y27 = request.POST.get('Y26')*6
        load.y29 = request.POST.get('Y28')*30
        load.y31 = request.POST.get('Y30')*0.6
        load.y32 = request.POST.get('Y32')
        load.y34 = request.POST.get('Y33')*80
        load.y36 = request.POST.get('Y35')*50
        load.y38 = request.POST.get('Y37')*80
        load.y39 = request.POST.get('Y39')
        load.y41 = request.POST.get('Y40')*0.33
        load.y43 = request.POST.get('Y42')*24
        load.y45 = request.POST.get('Y44')*12
        load.y47 = request.POST.get('Y46')*30
        load.y49 = request.POST.get('Y48')*0.18
        load.y50 = request.POST.get('Y50')
        load.y51 = request.POST.get('Y51')
        load.y53 = request.POST.get('Y52')*3
        load.y532 = request.POST.get('Y522')*1
        load.y55 = request.POST.get('Y54')*2
        load.y57 = request.POST.get('Y56')*3
        load.y59 = request.POST.get('Y58')*1
        load.y61 = request.POST.get('Y60')*2
        load.y63 = request.POST.get('Y62')*1
        load.y65 = request.POST.get('Y64')*2
        load.y67 = request.POST.get('Y66')*3
        load.y69 = request.POST.get('Y68')*1
        load.y71 = request.POST.get('Y70')*0.5
        load.y731 = request.POST.get('Y721')*6
        load.y732 = request.POST.get('Y722')*6
        load.y733 = request.POST.get('Y723')*6
        load.y734 = request.POST.get('Y724')*6
        load.y75 = request.POST.get('Y75')
        load.y76 = request.POST.get('Y76')
        load.y77 = request.POST.get('Y77')
        load.y79 = request.POST.get('Y78')*7
        load.y80 = request.POST.get('Y80')
        load.y82 = request.POST.get('Y81')*12
        load.y84 = request.POST.get('Y83')*6
        load.y86 = request.POST.get('Y85')*30
        load.y88 = request.POST.get('Y87')
        load.y90 = request.POST.get('Y89')
        load.y92 = request.POST.get('Y91')
        load.y94 = request.POST.get('Y93')
        load.y96 = request.POST.get('Y95')
        load.y98 = request.POST.get('Y97')*5
        load.y99 = request.POST.get('Y99')
        load.y100 = request.POST.get('Y100')
        load.y102 = request.POST.get('Y101')*30
        # Научная нагрузка
        load.z = request.POST.get('Z')
        load.z2 = request.POST.get('Z1')*70
        load.z4 = request.POST.get('Z3')*90
        load.z6 = request.POST.get('Z5')*50
        load.z8 = request.POST.get('Z7')*70
        load.z10 = request.POST.get('Z9')*40
        load.z12 = request.POST.get('Z11')*100
        load.z13 = request.POST.get('Z13')
        load.z14 = request.POST.get('Z14')
        load.z15 = request.POST.get('Z15')
        load.z16 = request.POST.get('Z16')
        load.z18 = request.POST.get('Z17')*90
        load.z19 = request.POST.get('Z19')
        load.z20 = request.POST.get('Z20')
        load.z21 = request.POST.get('Z21')
        load.z23 = request.POST.get('Z22')*10
        load.z25 = request.POST.get('Z24')*40
        load.z27 = request.POST.get('Z26')*50
        load.z29 = request.POST.get('Z28')*6
        load.z31 = request.POST.get('Z30')*12
        load.z33 = request.POST.get('Z32')*7
        load.z36 = request.POST.get('Z34')*request.POST.get('Z35')
        load.z38 = request.POST.get('Z37')*25
        # Командирская подготовка
        load.f1 = request.POST.get('F1')
        load.f2 = request.POST.get('F2')
        load.f3 = request.POST.get('F3')
        load.f4 = request.POST.get('F4')
        load.f5 = request.POST.get('F5')
        load.f6 = request.POST.get('F6')
        # Другие виды работ
        load.g1 = request.POST.get('G1')
        load.g2 = request.POST.get('G2')

        return render(request, "calculation.html")

