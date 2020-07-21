from . import views
from django.urls import path
from .views import PostListView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="demos-home"),
    path('home/', views.home, name="demos-home"),
    path('about/',views.about , name="demos-about"),
    path('get/',views.home , name="demos-home"),

]
