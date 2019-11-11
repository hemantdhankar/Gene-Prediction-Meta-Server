from django.http import HttpResponse
from django.shortcuts import render
from .functions import *
import os
from pathlib import Path


def home(request):
	if request.method == 'POST':
		handle_uploaded_file(request.FILES['file'])
		os.path.abspath('..')
		os.chdir("static/upload/")
		os.system(" python3 geneidscript.py")
		send_email(request.POST['email'])
		return HttpResponse("File uploaded successfuly")  
	else:  
		return render(request,"home.html")