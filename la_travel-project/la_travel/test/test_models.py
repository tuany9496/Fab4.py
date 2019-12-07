from search.models import Place
from mixer.backend.django import mixer
from django.test import TestCase
import pytest



@pytest.mark.django_db
class TestModels (TestCase):

    @staticmethod
    def enter_data():
        places = Place.objects.create()
        places.companyName = 'TestCompany'
        places.addressName = 'TestAddress'
        places.cityName = 'TestCity'
        places.Rating = '2.1'
        places.save()

        return places

    def test_places(self):
        places = self.enter_data()
        self.assertTrue(isinstance(places, Place))
        assert places.companyName == 'TestCompany'

# @pytest.mark.django_db
# def test_db_count():
#     assert Place.objects.count() ==0

#
# @pytest.mark.django_db
# class TestModels:
#     def
#     def test_db_add_restaurant():
#         r1 = Place.objects.create(
#             companyName='TestName',
#             addressName='TestAddress'
#         )
#         assert r1.companyName == 'TestName'
# def test_last_database_record (pboject_instance):
#     assert Place[1476].companyName =='2 Musketeers Pizza Inc'
# class TestModels:
#
#     # Test correct view
#     def test_db_size(Place):
#         #stmt = 'SELECT * FROM Place'
#         #rs = Place.execute(stmt).fetchall()
#         places = Place.all()
#         assert len (places) == 1477
