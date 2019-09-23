from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.


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

# Number of visits to this view, as counted in the session variable.
    # 방문자 숫자 체크하는 세션
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'specific_num_books': specific_num_books,
        'specific_num_genre': specific_num_genre,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):  # generic list view - 조건에 맞는 여러 객체를 리스트로
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
