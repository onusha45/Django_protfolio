from django.shortcuts import render
from django.http import HttpResponse
from .models import*
# Create your views here.

def contact(request):
    return render(request,"contact.html")

def Savecontact(request):

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        content = request.POST['content']
        

        Contactus = Contact(fname=fname, lname=lname, email=email, content=content)
        Contactus.save()

        print(f"Received form data - fname: {{fname}}, Last Name: {{lname}},Email: {{email}}, content: {{content}}")
        return render(request, 'contact.html')
