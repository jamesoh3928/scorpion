from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin    


def vacation(request):
    return render(request, 'vacation/vacationHome.html')
