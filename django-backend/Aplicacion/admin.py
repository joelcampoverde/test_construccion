from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Propiedad)
admin.site.register(Medidor)
admin.site.register(Tarifa)
admin.site.register(Lectura)
admin.site.register(Concepto)
