from __future__ import absolute_import
from celery import shared_task
from DaemonApp.models import *
from OrderManagement.EmailEngine.EmailEngine.CeleryTasks import send_mail
from OrderManagement.SmsEngine.SmsEngine.CeleryTasks import send_sms
from django.forms.models import model_to_dict
from django.db.models import Q



def service():
	notifications = NotificationRetry.objects.filter(Q(mail_sent=False || sms_sent=False))
	for notification in notifications:
		send_mail.apply_async(args=[notification.id],)
		send_sms.apply_async(args=[notification.id],)


service()



