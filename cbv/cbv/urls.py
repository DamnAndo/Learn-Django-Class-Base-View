
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',WelcomeView.as_view()),
    path('accounts/',include('django.contrib.auth.urls'))
]
