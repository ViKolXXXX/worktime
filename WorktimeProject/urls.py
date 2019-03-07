
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('igbrv.urls')),
    # path(r'^accounts/', include('django.contrib.auth.urls')),
]
