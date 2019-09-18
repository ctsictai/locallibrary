from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.


class BookListView(generic.ListView):
    model = Book

    # your own name for the list as a template variable
    context_object_name = 'my_book_list'
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book


def index(request):
    # View function for home page of site.

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # specific word in title - "rings"
    specific_num_books = Book.objects.filter(title__icontains='rings').count()

    # specific word in genre - "human"
    specific_num_genre = Genre.objects.filter(name__icontains='Human').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'specific_num_books': specific_num_books,
        'specific_num_genre': specific_num_genre,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)
