"""
URL configuration for django_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'), # esta vista es la que redireccionamos al usuario que se creo
    path('tasks/create/', views.crear_tarea, name='crear_tarea'),  #esta vista es para los usarios que ya estan registrado
    path('tasks/<int:id>/', views.detalletarea, name='detalletarea'),
    path('tasks/<int:id>/complete', views.tareaCompleta, name='tareacompleta'), #este metodo sirve para completar la tarea
    path('tasks/<int:id>/eliminar', views.tareaEliminada, name='tareaeliminada'), #este metodo sirve para eliminar la tarea
    path('cerrarsesion/', views.cierreSesion, name='cerrarsesion'),  #esta vista cierra la sesio
    path('signin/', views.signin, name='signin'),  #esta vista muestra ell formulario para ingresar
    path('mostrartodas/', views.todaslasTareas, name='todastareas'),  #esta vista es para los usarios que ya estan registrado
    

]
