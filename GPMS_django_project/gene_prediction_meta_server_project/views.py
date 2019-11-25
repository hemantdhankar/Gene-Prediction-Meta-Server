from django.http import HttpResponse
from django.shortcuts import render
from threading import Thread
from .functions import run_task
def home(request):
	if request.method == 'POST': 
		background_thread=Thread(target=run_task, args=(request,))
		background_thread.daemon=True
		background_thread.start()
		return HttpResponse("You will recieve the mail soon")  
	else:  
		return render(request,"home.html")