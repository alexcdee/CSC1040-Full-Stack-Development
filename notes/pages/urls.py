from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    

    path('users/<int:id>/', views.user_profile, name='user_profile'),
    path('search/<category>/', views.search),

    # books page
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/add/', views.add_book, name='add_book'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]