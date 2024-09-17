#admin nos ayuda a gestionar los modelos creado desde una interfaz web sin necesidad de crearla

from django.contrib import admin
from .models import To_do

# Register your models here.

admin.site.register(To_do)  #Hacemos gestionable desde el panel de administración (Manipular los datos)

#luego procedemos a crear un admin user y password para su correcto log in