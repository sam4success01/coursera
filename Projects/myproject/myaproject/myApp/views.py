from django.shortcuts import render

from myApp.forms import LogForm, DemoForm

# Create your views here.

from django.http import HttpResponse
from django.db import models
from datetime import datetime
from myApp.models import NewMenus


def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "home.html", context)

def about(request):
    about_content = {'about': "Based in Chicago, Illinois, Little lemon is the best company"}
    return render(request, "about.html", about_content)

def menu(request):
    menuitem = {'mains': [
        {'name':'falafel', 'price': '12'},
        {'name':'shawarma', 'price': '15'},
        {'name':'gyro', 'price': '10'},
    ]}
    return render(request, 'menu.html', menuitem)

def menu_by_id(request):
    menuitem = NewMenus.objects.all()
    newmenu_dict = {'menuitem': menuitem}
    return render(request, 'menuid.html', newmenu_dict)



def Demo_form(request):
    Demo = DemoForm()
    contexts = {"demo" : Demo}
    return render(request, "home.html", contexts)



def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
    <br>Path: {path}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>Address: {address}
    <br>User Agent: {user_agent}
    <br>Path Info: {path_info}
    <br>Response Header: {response.headers}
    """
    
    return HttpResponse(msg, content_type="text/html", charset="utf-8")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menus(request):
    text = """<h1 style="color: #F4CE14">This is little lemon again!</h1>"""
    return HttpResponse(text)

def menuitems(request, dish):
    items = {
        'pasta' : 'Pasta is a type of noodle from combination of',
        'falafel' : 'Falafel are deep fried patties or balls made',
        'chesecake' : 'Cheesecake is a type of dessert made with'
    }
    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)
