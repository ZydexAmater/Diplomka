from django.urls import path
from zydex import views
from django.contrib.auth.views import LogoutView

app_name = 'zydex'

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth_view, name='auth'),
    path('about/', views.about, name='about'),
    path('nurse/', views.nurse_visit_view, name='nurse_visit'),
    path('nurse/success/', views.visit_success, name='visit_success'),
    path('nurse/visits/', views.nurse_visit_list, name='nurse_visit_list'),
    path('nurse/edit/<int:pk>/', views.edit_visit, name='edit_visit'),
    path('nurse/delete/<int:pk>/', views.delete_visit, name='delete_visit'),
    path('logout/', LogoutView.as_view(next_page='zydex:auth'), name='logout'),
]
