from django.shortcuts import render
from django.db.models import Q
from hotels.models import hotels

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        print(submitbutton)
        if query is not None:
            lookups= Q(city__icontains=query) | Q(street__icontains=query)

            results= hotels.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search_result.html', context)

        else:
            return render(request, 'search_result.html')

    else:
        return render(request, 'search_result.html')