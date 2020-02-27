from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from intake.models import Client
from .helpers import get_ajax_search_results


@login_required
def home(request):
    context = get_ajax_search_results(request, Client)
    if request.is_ajax():
        html = render_to_string(
            template_name='intake/includes/partial_client_home.html',
            context=context
        )
        data_dict = {"html_model_list": html}
        return JsonResponse(data=data_dict, safe=False)
    else:
        return render(request, 'core/home.html', context)
