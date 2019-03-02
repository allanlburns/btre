from django.shortcuts import render

def index(request):
	return render(request, 'listings/listings.html')

def listing(self):
	return render(request, 'listings/listing.html')

def search(self):
	return render(request, 'listings/search.html')
