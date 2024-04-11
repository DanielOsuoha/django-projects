from . import views
from django.urls import path

urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path('', views.home, name='home'),
    path('create', views.create, name= 'create'),
    path('handle', views.handleitem, name='handle'),
    path('view', views.view, name='view')
]
