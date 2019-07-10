from behave import given, then, when
from django.conf import settings

from cases.tests.functional.create_session import \
    create_pre_authenticated_session


@given(u'I am a logged-in user with the correct permissions')
def given_i_am_logged_in(context):
    session_key = create_pre_authenticated_session(email='drug_court_user@drug_court.com')
    context.browser.get(context.get_url('/404_does_not_exist/'))
    context.browser.add_cookie(dict(
        name=settings.SESSION_COOKIE_NAME,
        value=session_key,
        path='/'
    ))


@when(u'I create a client with "{first_name}"')
def create_a_client(context, first_name):
    import pdb
    pdb.set_trace()

    context.browser.get(context.get_url('/cases/intake/'))
    context.browser.find_element_by_id('id_client-first_name').send_keys(first_name)


    raise NotImplementedError(u'STEP: When I create a Client')


@when(u'I add a Referral')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I add a Referral')


@when(u'I add a Note')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I add a Note')


@then(u'I will be redirected to the Client Detail View')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I will be redirected to the Client Detail View')
