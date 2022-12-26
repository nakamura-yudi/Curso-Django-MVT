from django.urls import path
from . import views


urlpatterns = [
    path('cadastro', views.cadastro, name="cadastroUsuario"),
    path('login', views.login, name="login"),
    path('dashbord', views.dashbord, name="dashbord"),
    path('logout', views.logout, name="logout"),

]