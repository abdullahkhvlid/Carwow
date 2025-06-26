from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from datetime import datetime
from home.models import Signup



# Create your views here.


def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        c= Signup(email= email, password=password, date=datetime.today())
        c.save()
        messages.success(request, "YOU HAVE SIGNED UP")

    
    return render(request, "signup.html")




def index(request):
    
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        c = Contact(name=name, email=email, message=message, date=datetime.today())
        c.save()
        messages.success(request, "THANK YOU FOR CONTACTING US, WE WILL GET BACK TO YOU SOON")
        

        
    return render(request, "contact.html")


from django.template.loader import render_to_string
from django.conf import settings
import os

def search(request):
    if request.method == "GET":
        query = request.GET.get("q", "").lower()
        templates_path = os.path.join(settings.BASE_DIR, "templates")

        # filenames mapped to page title
        html_pages = {
            "about.html": "About Page",
            "contact.html": "Contact Page",
            "index.html": "Home Page",
            "services.html": "Services Page",
        }

        for filename, title in html_pages.items():
            file_path = os.path.join(templates_path, filename)
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    if query in content.lower():
                        highlighted = content.replace(query, f"<mark>{query}</mark>")
                        return HttpResponse(highlighted)  # directly show page with highlight

        return HttpResponse("No results found")
    



def inventory(request):
    return render(request, "inventory.html")