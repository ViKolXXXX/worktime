from django.contrib.auth.decorators import login_required
from django.urls import re_path

from igbrv.views import auth_view
from igbrv.views.about_view import AboutView
from igbrv.views.archive_view import ArchiveView
from igbrv.views.calculation_academic_view import CalculationAcademicView
from igbrv.views.calculation_commander_view import CalculationCommanderView
from igbrv.views.calculation_methodical_view import CalculationMethodicalView
from igbrv.views.calculation_other_view import CalculationOtherView
from igbrv.views.calculation_science_view import CalculationScienceView
from igbrv.views.index_view import IndexView

urlpatterns = [
    re_path(r'^$', login_required(IndexView.as_view()), name="index"),
    re_path(r'^about$', login_required(AboutView.as_view()), name="about"),
    re_path(r'^archive$', login_required(ArchiveView.as_view()), name="archive"),
    re_path(r'^calculation-academic$', login_required(CalculationAcademicView.as_view()), name="calculation-academic"),
    re_path(r'^calculation-commander$', login_required(CalculationCommanderView.as_view()), name="calculation-commander"),
    re_path(r'^calculation-methodical$', login_required(CalculationMethodicalView.as_view()), name="calculation-methodical"),
    re_path(r'^calculation-other$', login_required(CalculationOtherView.as_view()), name="calculation-other"),
    re_path(r'^calculation-science$', login_required(CalculationScienceView.as_view()), name="calculation-science"),
    # Регистрация
    re_path(r'^register/', auth_view.RegisterFormView.as_view(), name="register"),
    re_path(r'^login/', auth_view.LoginFormView.as_view(), name="login"),
    re_path(r'^logout/', auth_view.LogoutView.as_view(), name="logout"),
]