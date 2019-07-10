
        # TODO: Have to pass self to render_to_response to get this to pass
        # kwargs = {'client_form': mock_get.return_value, 'note_form': mock_get.return_value,
        #                                 'referral_form': mock_get.return_value}
        # mock_response.assert_called_once_with(kwargs)

        # @pytest.mark.django_db
        # class ReferralsDetailTest(WebTest):

        #     def setUp(self):
        #         self.request = RequestFactory().get('/fake-path')
        #         self.view = ReferralsUpdate
        #         self.view = setup_viewTest(self.view, self.request)

        #         self.client = Client()
        #         self.user = User.objects.create_user('john', 'johnpassword')
        #         # self.client.force_login(self.user)
        #         self.app.set_user(self.user)

        # # TODO: Test every action of methods

        #     # @patch(target='cases.forms.ReferralsDetail.post', autospec=True, ) # mock model imported from views.py
        #     def test_post_approve_button(self):
        #          # check if post with different name attributes are handled differently

        #         # this is going to throw a db access error
        #         form = ReferralsTabs()
        #         r = ReferralsFactory(refid=1000, status='Pending',
        #                              dadecision='Approved', defensedecision='Approved', teamdecision='Approved')

        #         # GET detail page response
        #         # get_response = self.client.get(f'/referrals/{r.refid}')
        #         # self.assertEqual(get_response.status, 200)

        #         # post_response = self.client.post(f'/referrals/{r.refid}', {'id': 'submit-id-approve'})
        #         # self.assertEqual(post_response.status, 200)
        #         # check decisions and status changed

        #     def test_post_approve(self):
        #         r = ReferralsFactory(pretrialdecision='Approved')
        #         response = self.app.get(r.get_absolute_url(), user='john')

        #         self.assertNotEqual(response.status_code, 404)

        #         form = self.app.get(r.get_absolute_url(), user='john').form
        #         form['dadecision'] = 'Approved'
        #         submit_form = form.submit('approve')
        #         pdb.set_trace()

        #         self.assertRedirects(submit_form, r.get_absolute_url())