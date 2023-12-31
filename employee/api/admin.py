from django.contrib import admin
from .models import Emp, Role, Dept

# Register your models here.

admin.site.register(Emp)
admin.site.register(Dept)
admin.site.register(Role)