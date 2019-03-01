from django.urls import re_path

from igbrv.views.about_view import AboutView
from igbrv.views.archive_view import ArchiveView
from igbrv.views.calculation_academic_view import CalculationAcademicView
from igbrv.views.calculation_commander_view import CalculationCommanderView
from igbrv.views.calculation_methodical_view import CalculationMethodicalView
from igbrv.views.calculation_other_view import CalculationOtherView
from igbrv.views.calculation_science_view import CalculationScienceView
from igbrv.views.index_view import IndexView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name="index"),
    re_path(r'^about$', AboutView.as_view(), name="about"),
    re_path(r'^archive$', ArchiveView.as_view(), name="archive"),
    re_path(r'^calculation-academic$', CalculationAcademicView.as_view(), name="calculation-academic"),
    re_path(r'^calculation-commander$', CalculationCommanderView.as_view(), name="calculation-commander"),
    re_path(r'^calculation-methodical$', CalculationMethodicalView.as_view(), name="calculation-methodical"),
    re_path(r'^calculation-other$', CalculationOtherView.as_view(), name="calculation-other"),
    re_path(r'^calculation-science$', CalculationScienceView.as_view(), name="calculation-science"),

]