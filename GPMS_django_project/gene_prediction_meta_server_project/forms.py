from django import forms  
class clientForm(forms.Form):   
    email = forms.EmailField(label="Enter Email")  
    file  = forms.FileField(label="Sequence File") # for creating file input  
