import json
from django.shortcuts import render
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Appvuln


def index(request):
	try:
		username = request.GET.get('username')
		password = request.GET.get('password')
		Appvuln.objects.create(vuln_name=username,vuln_url=password)
	except Exception as e:
		raise
	return HttpResponse(username+':'+password)
# @csrf_exempt
# def webhook(request):
# 	if request.method == 'GET':
# 		return HttpResponse("GET NOT ALLOW!")
# 	else:
# 		vul_data = json.loads(request.body)
# 		vuln = {}
# 		if 'detail' in str(request.body):
# 			host = vul_data.get('detail')['host']
# 			detail = vul_data.get('detail')['payload']
# 			target = vul_data.get('target')['url']
# 			vuln_class = vul_data['vuln_class']
# 			Appvuln.objects.create(vuln_name=vuln_class,vuln_url=target,vuln_detail=detail)
# 			#vuln_plugin = vul_data['plugin']
# 			#vuln_url = vul_data['target']['url']
# 			#vuln_type = vul_data['vuln_class']
# 			# Appvuln.objects.create(vuln_name=vuln_type,domain=vuln_url,)
# 			#print(vuln)

# 		else:
# 			print(vul_data)
# 			return HttpResponse("pass")
