from django.shortcuts import render, HttpResponse

# Create your views here.
def TodoList(request):
    return render(request,'index.html')