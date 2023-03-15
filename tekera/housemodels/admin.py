from django.contrib import admin
from .models import MyModel, Textures, Bin


@admin.register(MyModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions')


admin.site.register(Bin)
admin.site.register(Textures)
