from django.shortcuts import render
# Create your views here.
#view que renderiza indice
def indexView(request):
    return render(request, 'index.html', {})


