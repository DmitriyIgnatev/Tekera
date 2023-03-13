from django.contrib import admin
from .models import MyModel, Textures


@admin.register(MyModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions')


admin.site.register(Textures)
