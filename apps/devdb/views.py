from django.shortcuts import render

from .models import Developer

# Create your views here.
def index(request):
    # https://www.youtube.com/watch?v=Vhh_GeBPOhs
    developers = Developer.objects.all()
    return render(request, "devdb/index.html", {"developers": developers})