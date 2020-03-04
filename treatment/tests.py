from core.helpers import tests
from treatment import views

class AjaxViewTest(tests.SimpleTestCase):

    def test_save_client_form(self):
        """
            Test that client passed to form kwargs.
        """

        request = tests.RequestFactory().get('/fake-path')
        view = tests.setup_viewTest(views.client_create, request)
        self.assertIsInstance(request.context['form'], NoteForm)
        