from django.contrib import admin
from .models import MyModel, Textures, Bin, Application, Feedback, Layout


@admin.register(MyModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions')


admin.site.register(Bin)
admin.site.register(Textures)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'house')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'question')


admin.site.register(Layout)
