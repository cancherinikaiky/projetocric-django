from django.shortcuts import render

def charqueadas(resquest):
    return render(resquest, 'cities/charqueadas.html')

def vale_verde(request):
    return render(request, 'cities/vale_verde.html')

def cidade(request, post_name):
    name_filtered = post_name.lower().replace(" ", "_")
    return render(request, 'cities/' + name_filtered + '.html')
