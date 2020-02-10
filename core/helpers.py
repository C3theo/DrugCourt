import os
import shutil
from pathlib import Path

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

from intake.models import Client


def add_forms_to_context(forms, context):
    """
        Add multiple different forms to context, with
        model name as prefix.
    """

    context['forms'] = {
        f'{form.instance._meta.model_name}_form': form for form in forms}
    return context

def delete_all_migrations():
    """
        Delete migrations from all Apps.
    """
    base_path = Path(settings.BASE_DIR)
    migration_files = [each for each in base_path.glob(
        '../*/migrations/[!__init__]*.py')]

    for f in migration_files:
        os.unlink(f)



def save_ajax_form(request, form_template=None, list_template=None, context=None):
    """
        Helper function for validating multiple forms and
        adding to JsonResponse.
    """
    data = dict()

    if request.method == 'POST':
        valid_ctr = 0
        try:
            for _, form in context['forms'].items():
                if form.is_valid():
                    try: #ReferralForm
                        form.save(client=context['client'])

                    except (TypeError, KeyError):
                        form.save()

                    valid_ctr += 1
            
            if valid_ctr == len(context['forms']):
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False

        except (AttributeError, ):  # Decision Forms Generator
            for form in context['forms']:
                if form.is_valid():
                    form.save()
                    data['form_is_valid'] = True
    
    # Set first model in the context to the paginator

    model = context.items()[0]
    paginator_name = context.items()[0][1]._meta.verbose_name_plural
    paginator_name = paginator_name.replace(' ', '_').replace('ss', 's')
    model_class = model[1].__class__
    models = paginate_model(request, model_class)
    model_dict = {paginator_name: models}
    # import pdb; pdb.set_trace()
    # html_list = f'html_{model[0]}_list'
    html_list = 'html_model_list'
    

    data[html_list] = render_to_string(
        list_template, model_dict)

    data['html_form'] = render_to_string(form_template,
                                         context,
                                         request=request
                                         )
    # import pdb; pdb.set_trace()
    return JsonResponse(data)

    # save Note Form
    # try:
    #     # ???
    #     client = context['client']
    #     note = form.save(commit=False)
    #     note.author = request.user
    #     note.save()

    # except (KeyError, TypeError):
    #     form.save()


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
