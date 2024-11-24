from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('app.urls')),
    path('admin/', admin.site.urls),

    # Vue.js отдает index.html для маршрутизации через frontend
    path('', TemplateView.as_view(template_name="index.html")),
]
