from django.shortcuts import render , HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #esto es para crear el formulario y para ingresar
from django.contrib.auth.models import User  #esto es para guardar el usuario en la base de datos
from django.contrib.auth import login, logout, authenticate
from  .forms import TaskForm  #importamos el formulario creado
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required   #esto sirve para proteger las rutas


# Create your views here.
def home(request):
    return render(request,'home.html')

#este metodo sirve para registrar un usuario nuevo, dentro de try excepts usa login para guardar la sesion y redirecciona
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{'forms':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
          try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])#aca crea el usuario
                user.save()   #aca  lo guarda
                login(request,user)
                return redirect('tasks')
              
          except:
              return render(request,'signup.html',{'forms':UserCreationForm, 'error':'El Usuario ya existe'})

        
        return render(request,'signup.html',{'forms':UserCreationForm, 'error':'Las contraseñas no coiciden'})


#este metodo devuelve las tareas al front
@login_required
def tasks(request):
    tareas = Task.objects.filter(user=request.user,  datecompleted__isnull=True)  #aca pregunto si el usuario es igual al logeo y si la fecha de completo en nula
    return render(request, 'tasks.html', {'tareas':tareas})


#este metodo muestra todas las tareas completas
@login_required
def todaslasTareas(request):
    tareas = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'mostrartodas.html', {'tareas':tareas})

#este metodo crea una nueva tarea desde el front mediante el formulario de django
@login_required
def crear_tarea(request):
    if request.method == 'GET':
         return render(request, 'crearTarea.html',{'forms': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            nueva_tarea= form.save(commit=False)
            nueva_tarea.user=request.user
            nueva_tarea.save()
            return redirect('tasks')
        except:
            return render(request, 'crearTarea.html',{'forms': TaskForm, 'error':'Ingrese datos validos'})


#este metodo muestra el detalle de una tarea y a su vez lo usamos para actualizar
@login_required
def detalletarea(request, id):
    if request.method == 'GET':
          
          tarea= get_object_or_404(Task, pk=id, user=request.user)
          form = TaskForm(instance=tarea)
          return render(request,'detalletarea.html', {'tarea':tarea, 'form':form})
    else:
        tarea= get_object_or_404(Task, pk=id, user=request.user)
        form = TaskForm(request.POST, instance=tarea)
        form.save()
        return redirect('tasks')
  


#este metodo para una fecha al campo completado 
@login_required
def tareaCompleta(request, id):
    tarea= get_object_or_404(Task, id=id, user=request.user) #aca obtengo la tarea
    if request.method == 'POST':  #luego chequeo que sea post
        tarea.datecompleted= timezone.now()   #completo con la fecha actual
        tarea.save()
        return redirect('tasks')



#este metodo sirve para eliminar las tareas
@login_required
def tareaEliminada(request, id):
    tarea= get_object_or_404(Task, id=id, user=request.user) #aca obtengo la tarea
    if request.method == 'POST':  #luego chequeo que sea post
        tarea.delete()   #completo con la fecha actual
        return redirect('tasks')

        
   


#este metodo utiliza logout y es para cerra la sesion
def cierreSesion(request):
    logout(request)
    return redirect('home')

#este metodo sirve para buscar el usuario en la base de datos si lo encuentra guarda la sesio caso contrario devuelve un errror
def signin(request):
    if request.method == 'GET':
         return render(request, 'signin.html', {'form':AuthenticationForm})  # esta vista es para los usuarios que ya se registraron y quieren volver a entrar
    else:
        user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form':AuthenticationForm, 'error': 'Usuario o Password Incorrecto'})
        else:
            login(request, user) #Si lo encontro guardo la sesion y redirecciono
            return redirect('tasks')
        
       
       
        
        
        
                                      
