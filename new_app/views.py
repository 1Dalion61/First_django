from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index_page(request):
    context={
        "title": 'Курс "Промышленное программирование"',
        "name": 'Arseny',
        "count_page": '1'
    }
    return render(request, "index.html", context)

def time_page(request):
    now = datetime.now()
    context={
        "title": 'Курс "Промышленное программирование"',
        "current_date": now.strftime("%d/%m/%y"),
        "current_time": now.strftime("%H/%M/%S")
    }
    return render(request, "time.html", context)
