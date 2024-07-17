from django.urls import path
from . import views

urlpatterns = [
    path('del/<str:item_id>', views.remove, name='del'),
    path('', views.index, name='todo'),
]
