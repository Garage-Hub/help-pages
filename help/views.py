from django.shortcuts import render
import os

def single_page(request, category, slug):

    print(category)
    print(slug)

    content = open(os.path.dirname(__file__) + '/../data/%s/%s.md' % (category, slug)).read()

    return render(request, 'single.html', { 'content': content })
