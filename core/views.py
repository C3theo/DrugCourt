from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')


def ajax_search(request, model=None, template=None):
    context = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        models = model.objects.filter(name__icontains=url_parameter)
    else:
        models = model.objects.all()

    context["models"] = models

    return render(request, template, context=context)