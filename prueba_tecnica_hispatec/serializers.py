from rest_framework import serializers
from .models import Book, Category, Customer, Author, Book_lending

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['id', 'title', 'summary']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'name']

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ['name', 'surname', 'country', 'birth_date']

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['name', 'surname', 'country', 'birth_date']

class BoookLendingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book_lending
		fields = ['customer_id', 'book_id', 'lend_start_date', 'lend_expected_finish_date', 'lend_real_finish_date']