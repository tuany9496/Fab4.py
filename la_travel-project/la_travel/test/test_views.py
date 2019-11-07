from search import *
from django.test import RequestFactory
from django.urls import reverse
from search.views import *
from mixer.backend.django import mixer
from django.test import Client
import pytest

# Map is successful display
class TestViews:
    def test_map(self):
        path = reverse ('map')
        request = RequestFactory().get(path)
        response = home(request)
        assert response.status_code == 200

    def test_searched(self):
        path = reverse ('searched')
        request = RequestFactory().get(path)
        response = home(request)
        assert response.status_code == 200







    # def test_pass_client(self):
    #     c = Client()
    #     response = c.post ('/home/', 'search/home.html', {Where='Los Angeles', WhenFr='11/6/2019', WhenTo = '11/7/2019', What = 'Restaurants'})
    #     response = c.get('/searched/')
    #     response.content




    # def input_form_data(self.):
    #     Where = 'Los Angeles'
    #     WhenFr= '11/6/2019'
    #     WhenTo = '11/7/2019'
    #     What = 'Restaurants'



# soup = bs4.BeautifulSoup(content, 'html.parser')
# assert soup.select_one('h1#title-headliner') == '<h1>title</h1>'

# def test_map_page(self):
#     response = self.client.get (reverse('map'))
#     self.assertEquals(response.status_code, 200)
    #url = urls.reverse('map')
    #resp = self.client.get(url)
    #assert resp.status_code == 200
    #assert b'Login' in resp.content

#
# from mixer.backend.django import mixer
#
# import pytest
#
# from django.test import RequestFactory
#
#
# pytestmark = pytest.mark.django_db
#
# @pytest.fixture(scope="function")
# def fill_db():
#     """ Just filling the DB with my data """
#     for elem in services.Search().get_lookup_data():
#         mixer.blend('inventory.Enumeration', **elem)
#
# def test_grid_anonymous(fill_db):
#     request = RequestFactory().get('/grid/')
#     response = views.items_grid(request)
#     assert response.status_code == 200, \
#         "Should be callable by anyone"
#
# def test_list_anonymous(fill_db):
#     request = RequestFactory().get('/')
#     response = views.items_list(request)
#     assert response.status_code == 200, \
#         "Should be callable by anyone"
