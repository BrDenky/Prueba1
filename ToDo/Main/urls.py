from django.urls import path
from .views import CreateTo_Do, ReadTo_Do, UpdateTo_Do, DeleteTo_Do #Buenas prácticas el importar con nombre

urlpatterns = [
    #Accedemos a la tarea por su id, pk = primary key y actualiza la tarea con Put o patch
    path('<int:pk>/', UpdateTo_Do.as_view()),
    #Ruta Raiz, es decir que al enviar un Get nos devolverá la lista de todas las tareas
    path('', ReadTo_Do.as_view()),
    #Ruta que maneja la creación de nuevas tareas con una solicitud Post
    path('create/', CreateTo_Do.as_view()),
    #Ruta diseñada para eliminar una tarea específica por su id, por eso el <int:pk>
    path('delete/<int:pk>/', DeleteTo_Do.as_view())
]