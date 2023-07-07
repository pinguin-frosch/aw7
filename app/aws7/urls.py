from django.contrib import admin
from django.urls import include, path

from aws7 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sobrecarga/', views.sobrecarga, name='sobrecarga'),
    path('tareas/', include('tareas.urls'))
]
