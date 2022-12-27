from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def books(request):
    template = 'books/books.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def books_pub_date(request, pub_date):
    books = Book.objects.order_by('pub_date')
    paginator = Paginator(books, 1)
    n = 1
    for book in books:
        if str(book.pub_date) == pub_date:
            break
        n += 1
    if n < 2:
        previous_page = None
        next_page = str(books[n].pub_date)
    elif n >= len(books):
        previous_page = str(books[n - 2].pub_date)
        next_page = None
    else:
        previous_page = str(books[n-2].pub_date)
        next_page = str(books[n].pub_date)
    page = paginator.get_page(n)
    template = 'books/books_pub_date.html'
    context = {'page': page,
               'previous_page': previous_page,
               'next_page': next_page}
    return render(request, template, context)


