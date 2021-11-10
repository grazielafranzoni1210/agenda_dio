from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', views.index), # para redirecionar a raiz do projeto para a agenda
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
