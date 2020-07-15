
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',WelcomeView.as_view())
]
