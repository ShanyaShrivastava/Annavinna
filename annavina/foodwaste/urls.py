from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.foodmart_list,name='index'),
    path('api',views.api,name='api'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login_view'),
    #path('logout',views.logout_view,name='logout'),
    path('foodmarts/', views.foodmart_list, name='foodmart_list'),
    path('foodmarts/add/', views.foodmart_add, name='foodmart_add'),
    path('foodmarts/<int:pk>/edit/', views.foodmart_edit, name='foodmart_edit'),
    path('map', views.map, name='map'),
    path('about/',views.about,name='about')
]
