from django.urls import path
from zydex import views

app_name = 'zydex'

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth_view, name='auth'),
    path('about/', views.about, name='about'),
]
