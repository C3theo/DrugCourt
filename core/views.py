from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework import viewsets

from intake.models import Client

from .helpers import get_ajax_search_results
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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
