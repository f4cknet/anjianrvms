from django.contrib import admin
from .models import Systemvuln,Appvuln

# Register your models here.
class SystemvulnAdmin(admin.ModelAdmin):
	list_display = ('vuln_name','ipaddress','vuln_level','vuln_process','vuln_handler','handler_phone','result','detect_time','done_time')

class AppvulnAdmin(admin.ModelAdmin):
	list_display = ('vuln_name','vuln_url','vuln_level','vuln_process','vuln_handler','handler_phone','result','detect_time','done_time')

admin.site.register(Systemvuln,SystemvulnAdmin)
admin.site.register(Appvuln,AppvulnAdmin)