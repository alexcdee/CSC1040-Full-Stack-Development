from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm
# Create your views here.

# Mock user data
USERS_DATA = {
    1: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    2: {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    3: {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'},
}

# user profile
def user_profile(request, id):
    user = USERS_DATA.get(id)
    if user is None:
        return render(request, 'not_found.html', {'id': id})
    
    return render(request, 'profile.html', {
        'user': user,
        'id': id
    })

# book list
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def book_search(request):
    query = request.GET.get('q', '') # get the 'q' parameter, default to empty string if not found
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none() # returns empty queryset if no search term
    return render(request, 'book_search.html', {'books': books, 'query': query})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'books': books})

# search view
def search(request, category):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    
    return render(request, 'search.html', {
        'category': category,
        'query': query,
        'page': page
    })


# ** PAGES ** 
# home page
def home(request):
    username = request.GET.get('username', 'Guest')
    return render(request, 'home.html', {
        'title': 'Welcome',
        'items': ['Django', 'Python', 'HTML'],
        'username': username,
        'users': USERS_DATA.values(),
    })

# about apge
def about(request):
    return render(request, 'about.html', {
        'title': 'About us',
        'description': 'Learn more about our company.',
    })

# contact page
def contact(request):
    return render(request, 'contact.html', {
        'title': 'Contact Us',
        'description': 'Contact us at: 123 456 789',
        "numbers": [1, 2, 3, 4, 5, 6, 7, 8],
    })