from django.contrib import admin
from .models import Machine,Domain

# Register your models here.
class MachineAdmin(admin.ModelAdmin):
	list_display = ('ipaddress','project','level','owner','owner_phone','level')

class DomainAdmin(admin.ModelAdmin):
	list_display = ('domain','project','level','owner','owner_phone','level')

admin.site.register(Machine,MachineAdmin)
admin.site.register(Domain,DomainAdmin)
