from django.shortcuts import render
from django.db.models import Q
from addBook.models import Book

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        print(submitbutton)
        if query is not None:
            lookups= Q(bname__icontains=query) | Q(description__icontains=query)

            results= Book.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search_result.html', context)

        else:
            return render(request, 'search_result.html')

    else:
        return render(request, 'search_result.html')