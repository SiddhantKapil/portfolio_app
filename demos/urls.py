from . import views
from django.urls import path
from .views import PostListView

urlpatterns = [
    path('', views.home, name="demos-home"),
    path('about/', views.about, name="demos-about"),
]
