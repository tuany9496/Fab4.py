import pytest

from django.urls import reverse, resolve

class TestUrls:

    # Test path / correct view returned
    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_signup_url(self):
        path = reverse('map')
        assert resolve(path).view_name == 'map'

    def test_login_url(self):
        path = reverse('searched')
        assert resolve(path).view_name == 'searched'
