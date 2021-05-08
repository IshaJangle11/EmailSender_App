from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth
import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# Create your views here.
def sendemail(request):
	if request.method =="POST":
		to=request.POST.get('toemail')
		subject=request.POST.get('subject')
		messege=request.POST.get('messege')
		#print(to,messege,subject)
		send_mail(
			#subject 
			subject,
			#msg
			messege,
			#fromemail
			settings.EMAIL_HOST_USER,
			#receivermail
			[to]
		)
		return render(
		request,
		'email.html',
		{

			'title' :'email sender'
		}
	    )

	else:
		return render(
		request,
		'email.html',
		{

			'title' :'email sender'
		}
	    )
	