from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from intake.models import Client
from django.conf import settings
from pathlib import Path
import shutil
import os



def delete_all_migrations():
    """
        Delete migrations from all Apps.
    """
    base_path = Path(settings.BASE_DIR)
    migration_files = [each for each in base_path.glob('../*/migrations/[!__init__]*.py')]
    
    for f in migration_files:
        os.unlink(f)
    
def save_ajax_form(request, form_template=None, list_template=None, context=None):
    """
        Helper function for validating multiple forms and
        adding to JsonResponse.
    """
    data = dict()

    # items = context.items()
    # forms = [items[1], items]
    if request.method == 'POST':
        valid_ctr = 0
        
        for _, form in context['forms'].items():
            if form.is_valid():
                form.save()
                valid_ctr += 1

            # save Note Form
            # try:
            #     # ???
            #     client = context['client']
            #     note = form.save(commit=False)
            #     note.author = request.user
            #     note.save()

            # except (KeyError, TypeError):
            #     form.save()

        if valid_ctr == len(context):
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    models = paginate_model(request, Client)
    model = context.items()[0]

    html_list = f'html_{model[0]}_list'
    # import pdb; pdb.set_trace()
    data[html_list] = render_to_string(
        list_template, {model[0]: models})

    data['html_form'] = render_to_string(form_template,
                                         context,
                                         request=request
                                         )

    return JsonResponse(data)

def paginate_model(request, model, count=25):

    model_list = model.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(model_list, count)

    try:
        models = paginator.page(page)
    except PageNotAnInteger:
        models = paginator.page(1)
    except EmptyPage:
        models = paginator.page(paginator.num_pages)

    return models
