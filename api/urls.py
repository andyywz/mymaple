from django.urls import path

from . import views

app_name = 'dailies'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:daily_id>/', views.show, name = 'show'),
]
