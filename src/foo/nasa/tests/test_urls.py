import foo.nasa.views
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foo.nasa.views import picture_of_day

class TestUrls(SimpleTestCase):
    def test_pod_url_is_resolved(self):
        url = reverse('pod')
        self.assertEquals(foo.nasa.views.picture_of_day, resolve(url).func)
