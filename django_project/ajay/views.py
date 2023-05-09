from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from ajay.models import Contact

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())

        #to save entry as name not as object1
        def __str__(self):
            return self.name
        contact.save()
    return render(request, 'contact.html')