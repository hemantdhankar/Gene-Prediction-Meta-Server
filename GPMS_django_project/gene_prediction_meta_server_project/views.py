from django.http import HttpResponse
from django.shortcuts import render
from .functions import *
import os
from pathlib import Path


def home(request):
	if request.method == 'POST':
		handle_uploaded_file(request.FILES['file'])
		softwares_list=request.POST.getlist('softwares[]')        
		if("1" in softwares_list or len(softwares_list)==0):
			print("s1")
			#os.path.abspath('..')
			#os.chdir("static/upload/")
			#os.system(" python3 geneidscript.py")

		if("2" in softwares_list):
			print("s2")
		if("3" in softwares_list):
			print("s3")
		x=request.POST["species"]
		send_email(request.POST['email'])
		return HttpResponse("File uploaded successfuly")  
	else:  
		return render(request,"home.html")