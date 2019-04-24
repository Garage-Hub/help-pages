from django.shortcuts import render

def single_page(request, category, slug):

    return render(request, 'single.html')
