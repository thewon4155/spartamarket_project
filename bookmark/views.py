from django.shortcuts import render

def bookmark_list(request):
    return render(request, 'bookmark/bookmark_list.html')

def bookmark_detail(request):
    return render(request, 'bookmark/bookmark_detail.html')

def bookmark_create(request):
    return render(request, 'bookmark/bookmark_create.html')
