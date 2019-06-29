from django.contrib import admin
from .models import Snack
# Register your models here.
@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ('id', 'v_nombre', 'v_tipo', 'i_precio')