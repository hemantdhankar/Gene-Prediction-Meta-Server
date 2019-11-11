from django.http import HttpResponse
from django.shortcuts import render
from .functions import handle_uploaded_file  
from .forms import clientForm
import os
from pathlib import Path

from pathlib import Path
def home(request):
	if request.method == 'POST':  
		client = clientForm(request.POST, request.FILES)
		if client.is_valid():  
			handle_uploaded_file(request.FILES['file']) 
			os.path.abspath('..')
			os.chdir("static/upload/")
			os.system(" python3 geneidscript.py")
			return HttpResponse("File uploaded successfuly")  
	else:  
		client = clientForm()  
		return render(request,"home.html",{'form':client})
