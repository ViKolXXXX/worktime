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
        # Учебная нагрузка
        load.x = int(self._check_on_none(request.POST.get('X')))
        # Методическая нагрузка
        load.y1 = float(self._check_on_none(request.POST.get('Y'))) * 0.5
        load.y3 = float(self._check_on_none(request.POST.get('Y2'))) * 0.2
        load.y5 = float(self._check_on_none(request.POST.get('Y4'))) * 0.3
        load.y7 = int(self._check_on_none(request.POST.get('Y6'))) * 70
        load.y9 = int(self._check_on_none(request.POST.get('Y8'))) * 90
        load.y11 = int(self._check_on_none(request.POST.get('Y10'))) * 35
        load.y13 = int(self._check_on_none(request.POST.get('Y12'))) * 45
        load.y15 = int(self._check_on_none(request.POST.get('Y14'))) * 3
        load.y17 = int(self._check_on_none(request.POST.get('Y16'))) * 12
        load.y19 = int(self._check_on_none(request.POST.get('Y18'))) * 6
        load.y21 = int(self._check_on_none(request.POST.get('Y20'))) * 40
        load.y23 = int(self._check_on_none(request.POST.get('Y22'))) * 20
        load.y25 = int(self._check_on_none(request.POST.get('Y24'))) * 10
        load.y27 = int(self._check_on_none(request.POST.get('Y26'))) * 6
        load.y29 = int(self._check_on_none(request.POST.get('Y28'))) * 30
        load.y31 = float(self._check_on_none(request.POST.get('Y30'))) * 0.6
        load.y32 = int(self._check_on_none(request.POST.get('Y32')))
        load.y34 = int(self._check_on_none(request.POST.get('Y33'))) * 80
        load.y36 = int(self._check_on_none(request.POST.get('Y35'))) * 50
        load.y38 = int(self._check_on_none(request.POST.get('Y37'))) * 80
        load.y39 = int(self._check_on_none(request.POST.get('Y39')))
        load.y41 = float(self._check_on_none(request.POST.get('Y40'))) * 0.33
        load.y43 = int(self._check_on_none(request.POST.get('Y42'))) * 24
        load.y45 = int(self._check_on_none(request.POST.get('Y44'))) * 12
        load.y47 = int(self._check_on_none(request.POST.get('Y46'))) * 30
        load.y49 = float(self._check_on_none(request.POST.get('Y48'))) * 0.18
        load.y50 = int(self._check_on_none(request.POST.get('Y50')))
        load.y51 = int(self._check_on_none(request.POST.get('Y51')))
        load.y53 = int(self._check_on_none(request.POST.get('Y52'))) * 3
        load.y532 = int(self._check_on_none(request.POST.get('Y522'))) * 1
        load.y55 = int(self._check_on_none(request.POST.get('Y54'))) * 2
        load.y57 = int(self._check_on_none(request.POST.get('Y56'))) * 3
        load.y59 = int(self._check_on_none(request.POST.get('Y58'))) * 1
        load.y61 = int(self._check_on_none(request.POST.get('Y60'))) * 2
        load.y63 = int(self._check_on_none(request.POST.get('Y62'))) * 1
        load.y65 = int(self._check_on_none(request.POST.get('Y64'))) * 2
        load.y67 = int(self._check_on_none(request.POST.get('Y66'))) * 3
        load.y69 = int(self._check_on_none(request.POST.get('Y68'))) * 1
        load.y71 = float(self._check_on_none(request.POST.get('Y70'))) * 0.5
        load.y731 = int(self._check_on_none(request.POST.get('Y721'))) * 6
        load.y732 = int(self._check_on_none(request.POST.get('Y722'))) * 6
        load.y733 = int(self._check_on_none(request.POST.get('Y723'))) * 6
        load.y734 = int(self._check_on_none(request.POST.get('Y724'))) * 6
        load.y75 = int(self._check_on_none(request.POST.get('Y75')))
        load.y76 = int(self._check_on_none(request.POST.get('Y76')))
        load.y77 = int(self._check_on_none(request.POST.get('Y77')))
        load.y79 = int(self._check_on_none(request.POST.get('Y78'))) * 7
        load.y80 = int(self._check_on_none(request.POST.get('Y80')))
        load.y82 = int(self._check_on_none(request.POST.get('Y81'))) * 12
        load.y84 = int(self._check_on_none(request.POST.get('Y83'))) * 6
        load.y86 = int(self._check_on_none(request.POST.get('Y85'))) * 30
        load.y88 = int(self._check_on_none(request.POST.get('Y87')))
        load.y90 = int(self._check_on_none(request.POST.get('Y89')))
        load.y92 = int(self._check_on_none(request.POST.get('Y91')))
        load.y94 = int(self._check_on_none(request.POST.get('Y93')))
        load.y96 = int(self._check_on_none(request.POST.get('Y95')))
        load.y98 = int(self._check_on_none(request.POST.get('Y97'))) * 5
        load.y99 = int(self._check_on_none(request.POST.get('Y99')))
        load.y100 = int(self._check_on_none(request.POST.get('Y100')))
        load.y102 = int(self._check_on_none(request.POST.get('Y101'))) * 30
        # Научная нагрузка
        load.z = int(self._check_on_none(request.POST.get('Z')))
        load.z2 = int(self._check_on_none(request.POST.get('Z1'))) * 70
        load.z4 = int(self._check_on_none(request.POST.get('Z3'))) * 90
        load.z6 = int(self._check_on_none(request.POST.get('Z5'))) * 50
        load.z8 = int(self._check_on_none(request.POST.get('Z7'))) * 70
        load.z10 = int(self._check_on_none(request.POST.get('Z9'))) * 40
        load.z12 = int(self._check_on_none(request.POST.get('Z11'))) * 100
        load.z13 = int(self._check_on_none(request.POST.get('Z13')))
        load.z14 = int(self._check_on_none(request.POST.get('Z14')))
        load.z15 = int(self._check_on_none(request.POST.get('Z15')))
        load.z16 = int(self._check_on_none(request.POST.get('Z16')))
        load.z18 = int(self._check_on_none(request.POST.get('Z17'))) * 90
        load.z19 = int(self._check_on_none(request.POST.get('Z19')))
        load.z20 = int(self._check_on_none(request.POST.get('Z20')))
        load.z21 = int(self._check_on_none(request.POST.get('Z21')))
        load.z23 = int(self._check_on_none(request.POST.get('Z22'))) * 10
        load.z25 = int(self._check_on_none(request.POST.get('Z24'))) * 40
        load.z27 = int(self._check_on_none(request.POST.get('Z26'))) * 50
        load.z29 = int(self._check_on_none(request.POST.get('Z28'))) * 6
        load.z31 = int(self._check_on_none(request.POST.get('Z30'))) * 12
        load.z33 = int(self._check_on_none(request.POST.get('Z32'))) * 7
        load.z36 = int(self._check_on_none(request.POST.get('Z34'))) * int(self._check_on_none(request.POST.get('Z35')))
        load.z38 = int(self._check_on_none(request.POST.get('Z37'))) * 25
        # Командирская подготовка
        load.f1 = int(self._check_on_none(request.POST.get('F1')))
        load.f2 = int(self._check_on_none(request.POST.get('F2')))
        load.f3 = int(self._check_on_none(request.POST.get('F3')))
        load.f4 = int(self._check_on_none(request.POST.get('F4')))
        load.f5 = int(self._check_on_none(request.POST.get('F5')))
        load.f6 = int(self._check_on_none(request.POST.get('F6')))
        # Другие виды работ
        load.g1 = int(self._check_on_none(request.POST.get('G1')))
        load.g2 = int(self._check_on_none(request.POST.get('G2')))

        load.user = request.user

        load.save()

        return render(request, "archive.html")

    def _check_on_none(self, enter_number):
        if enter_number is None:
            return 0
        else:
            return enter_number

