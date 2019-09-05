from django.test import TestCase, Client
from django.urls import reverse


class ResultViewTestCase(TestCase):

    def setUp(self):
        self.url = '/result/{0}/{1}/'
        self.client = Client()

    def test_view_ok(self):
        response = self.client.get(self.url.format('2020', 'bissexto'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/result.html')

    def test_view_404(self):
        response = self.client.get(self.url.format('2020', 'naobissexto'))
        self.assertEquals(response.status_code, 404)

    def test_leap_context(self):
        response = self.client.get(self.url.format('2020', 'bissexto'))
        self.assertTrue('status' in response.context)
        self.assertEquals(response.context['status'], 'success')
        self.assertTrue('msg' in response.context)
        self.assertEquals(response.context['msg'], 'O ano 2020 é bissexto.')

    def test_no_leap_context(self):
        response = self.client.get(self.url.format('2019', 'nao-bissexto'))
        self.assertTrue('status' in response.context)
        self.assertEquals(response.context['status'], 'danger')
        self.assertTrue('msg' in response.context)
        self.assertEquals(response.context['msg'], 'O ano 2019 não é bissexto.')


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.url = '/'
        self.client = Client()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')