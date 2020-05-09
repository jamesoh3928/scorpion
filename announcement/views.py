from django.shortcuts import render

# Create your views here.
def announcement(request):
    return render(request, 'announcement/announcement.html')