from django.shortcuts import render

def search_post(request):
    if request.POST:
        te = request.POST['text']
    return render(request, 'myfirstvis/render.html')