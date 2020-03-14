from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

from intake.models import Client


def save_ajax_form(request, context=None):
    """
        Helper function for validating multiple forms and
        adding to JsonResponse.

        Args:

        Returns:
            data (dict):
    """

    data = dict()
    if request.method == 'POST':
        valid_ctr = 0
        # import pdb; pdb.set_trace()
        try:
            for _, form in context['forms'].items():
                if form.is_valid():
                    try:
                        # import pdb; pdb.set_trace()
                        model = form.save(**context['initial'])

                    except (TypeError, KeyError):
                        model = form.save()

                    valid_ctr += 1

            if valid_ctr == len(context['forms']):
                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False

        except (AttributeError, ):  #
            for form in context['forms']:
                if form.is_valid():
                    form.save()
                    data['form_is_valid'] = True
    return data


def render_ajax(request, context, data, form_template=None, list_template=None):
    """
        Renders Ajax form and table data.

        Args:
            request(HTTPRequest):
            context(dict):
            data(dict):
            form_template(str):
            list_template(str):

    """

    # Set first model in the context to the paginator
    model = context.items()[0]
    paginator_name = model[1]._meta.verbose_name_plural
    paginator_name = paginator_name.replace(' ', '_').replace('ss', 's')

    model_class = model[1].__class__
    models = model_class.objects.all().order_by('id')

    model_dict = {paginator_name: models}
    html_list = 'html_model_list'
    # data[html_list] = render_to_string(
    #     list_template, model_dict)
    # import pdb; pdb.set_trace()
    data['html_form'] = render_to_string(form_template,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def paginate_model(request, query, count=25):
    """

        Args:
            request(HTTPRequest):
            query(Query):
            count(int):
    """

    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(query, count)

        try:
            models = paginator.page(page)
        except PageNotAnInteger:
            models = paginator.page(1)
        except EmptyPage:
            models = paginator.page(paginator.num_pages)

    except TypeError:  # ???
        models = query.objects.all().order_by('id')

    return models


def get_ajax_search_results(request, model=None):
    context = {}
    url_parameter = request.GET.get("q")
    if url_parameter:
        models = model.objects.filter(last_name__icontains=url_parameter, ) | model.objects.filter(
            first_name__icontains=url_parameter, )
        models.order_by('id')
    else:
        models = model.objects.all().order_by('id')
    # paginator = paginate_model(request, models)

    context[model._meta.verbose_name_plural.replace('ss', 's')] = models
    return context


def add_forms_to_context(forms, context):
    """
        Add multiple different forms to context, with
        model name as prefix.
    """

    context['forms'] = {
        f'{form.instance._meta.model_name}_form': form for form in forms}
    return context
