from django.contrib import admin
from users.models import Person,User
# Register your models clase modelos here.

#admin.site.register(User)
admin.site.register(Person)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['user_nickname','user_password','user_active','person_id']
