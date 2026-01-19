from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'title': 'Welcome',
        'items': ['Django', 'Python', 'HTML'],
    })

def about(request):
    return render(request, 'about.html', {
        'title': 'About us',
        'description': 'Learn more about our company.',
    })

def contact(request):
    return render(request, 'contact.html', {
        'title': 'Contact Us',
        'description': 'Contact us at: 123 456 789',
        "numbers": [1, 2, 3, 4, 5],
    })