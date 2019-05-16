from django.contrib.auth.decorators import login_required
from django.urls import re_path, path

from igbrv.views import auth_view
from igbrv.views.about_view import AboutView
from igbrv.views.archive_view import ArchiveView
from igbrv.views.calculation_academic_view import CalculationAcademicView
from igbrv.views.calculation_commander_view import CalculationCommanderView
from igbrv.views.calculation_methodical_view import CalculationMethodicalView
from igbrv.views.calculation_other_view import CalculationOtherView
from igbrv.views.calculation_science_view import CalculationScienceView
from igbrv.views.calculation_view import CalculationView
from igbrv.views.del_load_view import DelLoadView
from igbrv.views.get_report1_view import GetReport1View
from igbrv.views.get_report2_view import GetReport2View
from igbrv.views.get_report3_view import GetReport3View
from igbrv.views.get_report4_view import GetReport4View
from igbrv.views.get_report5_view import GetReport5View
from igbrv.views.index_view import IndexView
from igbrv.views.report_view import ReportView

urlpatterns = [
    re_path(r'^$', login_required(IndexView.as_view()), name="index"),
    re_path(r'^about$', login_required(AboutView.as_view()), name="about"),
    path('report/<int:load_id>/', login_required(ReportView.as_view()), name="report"),
    path('report1/<int:load_id>/', login_required(GetReport1View.as_view()), name="report1"),
    path('report2/<int:load_id>/', login_required(GetReport2View.as_view()), name="report2"),
    path('report3/<int:load_id>/', login_required(GetReport3View.as_view()), name="report3"),
    path('report4/<int:load_id>/', login_required(GetReport4View.as_view()), name="report4"),
    path('report5/<int:load_id>/', login_required(GetReport5View.as_view()), name="report5"),
    re_path(r'^archive$', login_required(ArchiveView.as_view()), name="archive"),
    path('del-load/<int:load_id>/', login_required(DelLoadView.as_view()), name="del-load"),
    re_path(r'^calculation$', login_required(CalculationView.as_view()), name="calculation"),
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