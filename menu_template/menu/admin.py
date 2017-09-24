from django.contrib import admin

from .models import Menu
from .models import Item

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Menu, PersonAdmin)
admin.site.register(Item, PersonAdmin)
# Register your models here.
