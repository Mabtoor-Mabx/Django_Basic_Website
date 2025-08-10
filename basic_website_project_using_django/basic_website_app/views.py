from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title':  'Home page',
        'massage': 'Welcome To My Website',
        'items': ['Django', 'Python', 'Flask', 'MYSQL', 'STREAMLIT', 'ANVIL Works']
    }

    return render(request, 'home.html', context)

# About Page

def about(request):
    context = {
        'title': 'About Us',
        'description': "This Is Simple Django Applications Designed By Mabtoor Mabx"
    }

    return render(request, 'about.html', context)





