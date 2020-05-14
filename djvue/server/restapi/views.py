from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from datetime import datetime


def search(request):
    search_result=""
    genre_list = Genre.objects.all()
    if request.method == 'GET': # If the form is submitted
        if(request.GET.get('choice', None) = 'book'):
            search_result = Book.objects.all().order_by("book_name")
            search_result = search_result.filter(book_name=request.GET.get('search_box', ""))
            search_result = search_result.filter(isbn = request.GET.get('search_box_isbn', ""))
            search_result = search_result.filter(book_pages_number__range = (request.GET.get('min_pages', 0), request.GET.get('max_pages', 50000)))
            search_result = search_result.filter(book_language = request.GET.get('search_box_book_language', ""))
            search_result = search_result.filter(book_release_date__range = (request.GET.get('min_date', None), request.GET.get('max_date', datetime.now())))
            search_result = search_result.filter(genre__type__in=request.GET.getlist('genre', ""))
            search_result = search_result.filter(Q(author__first_name__contains=request.GET.get('first_name_search')) | Q(author__last_name__contains="last_name_search"))
        if(request.GET.get('editore', None)):
            search_result = Editor.objects.all().order_by('name')
            search_result = search_result.filter(name__contains=request.GET.get('search_box', ""))
            search_result = search_result.filter(country__name=request.GET.get('country', ""))
        if(request.GET.get('author', None)):
            search_result = Author.objects.all().order_by('last_name')
            search_result = search_result.filter(Q(first_name__contains=request.GET.get('search_box_first_name', "")) | Q(last_name__contains=request.GET.get('search_box_last_name', "")))
            search_result = search_result.filter(country_id__name=request.GET.get('country', ""))
    else:
        search_result = Book.objects.order_by('book_name')[:5]
    context = {'search_result': search_result,
                'genre_list': genre_list}
    return render(request, 'bookworm/search.html', context)
