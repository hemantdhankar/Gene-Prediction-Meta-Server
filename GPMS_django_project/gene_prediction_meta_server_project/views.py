from django.http import HttpResponse
from django.shortcuts import render
from .functions import *
from pathlib import Path
from threading import Thread

def home(request):
	if request.method == 'POST':
		handle_uploaded_file(request.FILES['file'])
		softwares_list=request.POST.getlist('softwares[]')        
		if("1" in softwares_list or len(softwares_list)==0):
			print("s1")
			background_thread=Thread(target=run_geneid, args=())
			background_thread.daemon=True
			background_thread.start()

		if("2" in softwares_list):
			print("s2")
		if("3" in softwares_list):
			print("s3")
		x=request.POST["species"]
		#send_email(request.POST['email'])
		return HttpResponse("You will recieve the mail soon")  
	else:  
		return render(request,"home.html")