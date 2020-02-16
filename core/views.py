from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')

def reset(request):
    return render(request, 'core/password_reset_form.html')
