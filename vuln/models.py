from django.db import models
from asset.models import Machine,Domain

# Create your models here.
class Systemvuln(models.Model):
	ipaddress = models.ForeignKey(Machine,db_column='ipaddress',on_delete=models.CASCADE,default='',primary_key=True)
	vuln_name = models.CharField('漏洞名称',max_length=15)
	vuln_detail = models.TextField()
	vuln_level = models.IntegerField('漏洞等级',choices=((1,"低危"),(2,"中危"),(3,"高危"),(4,"严重")))
	vuln_process = models.IntegerField('处理进度',default=1,choices=((1,"未处理"),(2,"处理中"),(3,"处理完成")))
	result = models.IntegerField('处理结果',choices=((1,"已修复"),(2,"已忽略"),(3,"已关机")))
	vuln_handler = models.CharField('漏洞经办人',max_length=15,null=True,blank=True)
	handler_phone = models.CharField('经办人电话',max_length=11,null=True,blank=True)
	#pub_date = models.DateTimeField(u'入库时间',editable = True)
	detect_time = models.DateTimeField('发现时间')
	done_time = models.DateTimeField('处理完成时间')

	class Meta:
		verbose_name = "系统漏洞"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.vuln_name

class Appvuln(models.Model):
	#domain = models.ForeignKey(Domain,db_column='domain',on_delete=models.CASCADE,default='',primary_key=True)
	vuln_name = models.CharField('漏洞名称',max_length=15)
	vuln_url = models.CharField('漏洞地址',max_length=250,primary_key=True)
	vuln_detail = models.TextField()
	vuln_level = models.IntegerField('漏洞等级',default='',choices=((1,"低危"),(2,"中危"),(3,"高危"),(4,"严重")))
	vuln_process = models.IntegerField('状态',default=1,choices=((1,"未处理"),(2,"处理中"),(3,"处理完成")))
	result = models.IntegerField('处理结果',choices=((1,"已修复"),(2,"已忽略")),null=True,blank=True)
	vuln_handler = models.CharField('漏洞经办人',max_length=15,null=True,blank=True)
	handler_phone = models.CharField('经办人电话',max_length=11,null=True,blank=True)
	#pub_date = models.DateTimeField(u'入库时间',editable = True)
	detect_time = models.DateTimeField('发现时间')
	done_time = models.DateTimeField('处理完成时间')

	class Meta:
		verbose_name = "应用程序漏洞"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.vuln_name
	