from django.urls import path
from housemodels import views

app_name = 'housemodels'
urlpatterns = [
    path('', views.home, name='housemodels'),
    path('login', views.login),
]