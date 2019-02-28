from django.urls import re_path

from calculation.views.index_view import IndexView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name="index"),
]