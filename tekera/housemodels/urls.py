from django.urls import path
from housemodels import views


app_name = 'housemodels'
urlpatterns = [
    path('', views.home, name='housemodels'),
    path('login', views.Login.as_view(template_name='login.html')),
    path('register', views.signup),
    path('logout', views.logout_view),
    path('main', views.main),
    path('detail/<int:pk>', views.detail, name='det')
]
