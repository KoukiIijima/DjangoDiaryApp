from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView, RedirectView
import apiv1.urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('accounts/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include(apiv1.urls.urlpatterns)),
    re_path(r'^/*', TemplateView.as_view(template_name='index.html')),
]
