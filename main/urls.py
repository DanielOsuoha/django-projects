from . import views
from django.urls import path

urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path('home', views.home, name='home'),
    path('', views.first, name='first'),
    path('create', views.create, name= 'create'),
    path('handle', views.handleitem, name='handle'),
    path('view', views.view, name='view')
]
