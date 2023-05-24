from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)  #puede estar vacío
    created= models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)  #lo comletamos nosotros y es opcional
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.titulo} por: {self.user.username}'
    
    class Meta:
        verbose_name='tarea'
        verbose_name_plural='Tareas'
