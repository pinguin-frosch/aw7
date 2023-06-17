from django.urls import path
from tareas import views

app_name = 'tareas'
urlpatterns = [
    path('', views.tareas, name='tareas'),
    path('agregar/', views.agregar, name='agregar'),
    path('<int:id>/eliminar', views.eliminar, name='eliminar'),
    path('<int:id>/actualizar', views.actualizar, name='actualizar')
]
