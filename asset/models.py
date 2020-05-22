from django.db import models

# Create your models here.
class Machine(models.Model):
	ipaddress = models.CharField('IP地址',max_length=15,primary_key=True)
	project = models.CharField('项目名称',max_length=250,null=True,blank=True)
	owner = models.CharField('资产联系人',max_length=50,null=True,blank=True)
	owner_phone = models.CharField('联系人电话',max_length=11,null=True,blank=True)
	level = models.IntegerField('资产重要性',default=2,choices=((1,"非常重要"),(2,"重要"),(3,"一般"),(4,"不重要")))
	#pub_date = models.DateTimeField(u'入库时间',editable = True)

	class Meta:
		verbose_name = "机器列表"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.ipaddress

class Domain(models.Model):
	domain = models.CharField('域名',max_length=50,primary_key=True)
	project = models.CharField('项目名称',max_length=250,null=True,blank=True)
	owner = models.CharField('项目联系人',max_length=50,null=True,blank=True)
	owner_phone = models.CharField('联系人电话',max_length=11,null=True,blank=True)
	level = models.IntegerField('业务重要性',default=2,choices=((1,"非常重要"),(2,"重要"),(3,"一般"),(4,"不重要")))
	
	class Meta:
		verbose_name = "域名列表"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.domain