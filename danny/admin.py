from django.contrib import admin
from .models import registration


# Register your models here.
class admin_register(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'contact_no', 'url_field')


admin.site.register(registration, admin_register)
