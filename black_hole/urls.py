from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from credit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('creadit/', views.index),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]
