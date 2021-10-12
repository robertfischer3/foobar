from django.test import TestCase, Client
from django.urls import reverse
from foo.nasa.models import PhotoOfDay
import json

class TestPodViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.pod_url = reverse('pod')

    def test_get_phot_of_day(self):
        response = self.client.get(self.pod_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pod.html')
