from django.urls import path

# from portfolio.port_app.views import customer, home
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('projects2/', views.projects2, name="projects2"),
    path('bio/', views.bio, name="bio"),
    path('trackFarm/', views.trackFarm, name="trackFarm"),
    path('thereapy/', views.thereapy, name="thereapy"),
    path('phpmotors/', views.phpmotors, name="phpmotors"),
    path('cages/', views.cages, name="cages"),
    path('purple/', views.purple, name="purple"),

    
]
