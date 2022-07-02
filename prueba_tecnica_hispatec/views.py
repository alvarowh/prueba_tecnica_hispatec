from django.http import JsonResponse
from .models import Book, Category, Customer, Author, Book_lending
from .serializers import BookSerializer, CategorySerializer, CustomerSerializer, AuthorSerializer, BoookLendingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_swagger import renderers
from rest_framework.decorators import api_view, renderer_classes


class BookCollection(APIView):
	@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
	@api_view(['GET','POST'])
	def book_list(request, format = None):

		if request.method == 'GET':
			books = Book.objects.all()
			serializer = BookSerializer(books, many=True)
			return Response(serializer.data)

		elif request.method == 'POST':
			serializer = BookSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)

	@api_view(['GET','PUT','DELETE'])
	def book_details(request,id, format = None):
		try:
			book = Book.objects.get(pk=id)
		except Book.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = BookSerializer(book)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = BookSerializer(book, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			book.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorCollection(APIView):
	@api_view(['GET','POST'])
	def author_list(request, format = None):

		if request.method == 'GET':
			authors = Author.objects.all()
			serializer = AuthorSerializer(authors, many=True)
			return Response(serializer.data)

		elif request.method == 'POST':
			serializer = AuthorSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)

	@api_view(['GET','PUT','DELETE'])
	def author_details(request,id, format = None):
		try:
			author = Author.objects.get(pk=id)
		except Author.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = AuthorSerializer(author)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = AuthorSerializer(author, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			author.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryCollection(APIView):

	@api_view(['GET','POST'])
	def category_list(request, format = None):

		if request.method == 'GET':
			categories = Category.objects.all()
			serializer = CategorySerializer(categories, many=True)
			return Response(serializer.data)

		elif request.method == 'POST':
			serializer = CategorySerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomerCollection(APIView):

	@api_view(['GET','POST'])
	def customer_list(request, format = None):

		if request.method == 'GET':
			customers = Customer.objects.all()
			serializer = CustomerSerializer(customers, many=True)
			return Response(serializer.data)

		elif request.method == 'POST':
			serializer = CustomerSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)

	@api_view(['GET','PUT','DELETE'])
	def customer_details(request,id, format = None):
		try:
			customer = Customer.objects.get(pk=id)
		except Customer.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = CustomerSerializer(customer)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = CustomerSerializer(customer, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			customer.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)


class BookLendingCollection(APIView):

	@api_view(['GET', 'POST'])
	def book_lending_list(request, format=None):

		if request.method == 'GET':
			book_lendings = Book_lending.objects.all()
			serializer = BoookLendingSerializer(book_lendings, many=True)
			return Response(serializer.data)

		elif request.method == 'POST':
			serializer = BoookLendingSerializer(data=request.data)
			if serializer.is_valid():
				if serializer.validated_data["lend_start_date"] < serializer.validated_data["lend_expected_finish_date"]:
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)
				else:
					return Response("Invalid Date", status.HTTP_400_BAD_REQUEST)

	@api_view(['GET', 'PUT', 'DELETE'])
	def book_lending_details(request, id, format=None):
		try:
			book_lending = Book_lending.objects.get(pk=id)
		except Book_lending.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = BoookLendingSerializer(book_lending)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = BoookLendingSerializer(book_lending, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		elif request.method == 'DELETE':
			book_lending.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)