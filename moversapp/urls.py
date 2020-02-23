from django . urls import path
from . import views


app_name = 'moversapp'


urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('(?P<driver_id>[0-9]+)/', views.detail, name='detail'),
    path('add_vehicle', views.add_vehicle, name='add_vehicle'),
    path('register/', views.register, name='register'),
    path('login/', views.login_driver, name='login_driver'),

]


