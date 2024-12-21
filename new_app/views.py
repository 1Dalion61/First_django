from django.shortcuts import render

# Create your views here.

def index_page(request):
    context={
        "title": 'Курс "Промышленное программирование"',
        "name": 'Arseny',
        "count_page": '1'
    }
    return render(request, "index.html", context)
