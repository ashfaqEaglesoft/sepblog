from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        "title":"Welcome to Eaglesoft Home Page",
        "bdata":"Welcome to Eaglesoft Python",
        "clist":["python","Web developemnt","Android","Graphic"],
        "details":[
                {"name":"Muhammad Ashfaq","role":"Programmer","salary":330},
                {"name":"Ansir Ali","role":"Graphic Designer","salary":35},
                {"name":"Zeeshan Ahmad","role":"App developer","salary":2203}
        ]
    }
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def course(request):
    return HttpResponse("Welcome to courses")

def coursedetails(request,courseid):
    return HttpResponse(courseid)
