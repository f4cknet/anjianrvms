# Generated by Django 2.2.2 on 2020-05-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuln', '0004_auto_20200522_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appvuln',
            name='done_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='处理完成时间'),
        ),
        migrations.AlterField(
            model_name='systemvuln',
            name='done_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='处理完成时间'),
        ),
    ]
