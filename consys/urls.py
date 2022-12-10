from django.contrib import admin
from django.urls import path
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('', views.index),
    path('logout/', views.logout_user),
    path('listagem/', views.listagem),
]
