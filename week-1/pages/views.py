from django.shortcuts import render

# Create your views here.

def user_profile(request, id):
    # IN a real app, you'd fetch this from a database
    users = {
        1: {'name': 'Alice', 'email': 'alice@example.com'},
        2: {'name': 'Bob', 'email': 'bob@example.com'},
        3: {'name': 'Charlie', 'email': 'charlie@example.com'},
    }
    
    user = users.get(id)
    if not user:
        return render(request, 'not_found.html', {'id': id})
    
    return render(request, 'profile.html', {'user_id': id})

def home(request):
    username = request.GET.get('username', 'Guest')
    return render(request, 'home.html', {
        'title': 'Welcome',
        'items': ['Django', 'Python', 'HTML'],
        'username': username,
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
        "numbers": [1, 2, 3, 4, 5, 6, 7, 8],
    })