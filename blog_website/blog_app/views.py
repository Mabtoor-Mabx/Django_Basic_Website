from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "My Blogs For Websites",
        "posts": [
            {"title" : "Monstro Rebafu", "content": "I am both a bit surprised and unsurprised that it’s been two years since last I posted anything on Hafuboti. I knew that I needed a break, but I had no idea that it would last as long as it has"},
            {"title": "Harold and the Creepy Purple Crayon", "content": "There are times that an idea tickles me enough that I have to follow it through and make it reality. When our Children’s Librarian Jennifer told me that the new book in Aaron"}
        ]
    }
    return render(request, 'blog/home.html', context)
