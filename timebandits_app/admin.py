"""Admin stuff for the site"""
from django.contrib import admin

# Register your models here.
from .models import Account, Charity, Task


class ReadIDAdmin(admin.ModelAdmin):
    """Lets us see the primary keys of models"""
    readonly_fields = ('id',)


admin.site.register(Account, ReadIDAdmin)
admin.site.register(Charity, ReadIDAdmin)
admin.site.register(Task, ReadIDAdmin)
