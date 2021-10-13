from django.contrib import admin
from usuario.models import Usuario,Roll
# Register your models here.

#admin.site.register(Usuario)
admin.site.register(Roll)

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin): #recibe un array de datos
    list_display=['name','firstname','age','status','roll_id']