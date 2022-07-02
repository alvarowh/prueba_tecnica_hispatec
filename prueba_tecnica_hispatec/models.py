from django.db import models



class Author(models.Model):
	name = models.CharField(max_length=120)
	surname = models.CharField(max_length=120)
	country = models.CharField(max_length=120)
	birth_date = models.DateField(default='1000-01-01', auto_now=False, editable=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length=120)
	surname = models.CharField(max_length=120)
	country = models.CharField(max_length=120)
	birth_date = models.DateField(default='1000-01-01', auto_now=False, editable=True)

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=200)
	summary = models.CharField(max_length=600)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.title

class Book_lending(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	lend_start_date = models.DateField(default='1000-01-01', auto_now=False, editable=True)
	lend_expected_finish_date = models.DateField(default='1000-01-01', auto_now=False, editable=True)
	lend_real_finish_date = models.DateField(default='1000-01-01', auto_now=False, editable=True)