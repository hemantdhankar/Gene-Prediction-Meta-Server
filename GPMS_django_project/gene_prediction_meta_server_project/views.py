from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import Process
from .functions import *
import time
def home(request):
	if request.method == 'POST':
		background_thread=Process(target=run_task, args=(request,))
		background_thread.daemon=True
		background_thread.start()
		return render(request,"submitted.html")  
	else:
		return render(request,"home.html")