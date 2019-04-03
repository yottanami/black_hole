from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from pardakht import urls as pardakht_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('pardakht.urls')),
    path('creadit/', include('credit.urls')),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
