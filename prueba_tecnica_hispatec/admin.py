from django.contrib import admin
from .models import Book, Category, Book_lending, Customer, Author

admin.site.register([Book, Category, Book_lending, Customer, Author])
