from django.test import TestCase
from helloapp.models import TestModel
import pytest


@pytest.mark.django_db
def test_helloworld():
    assert TestModel.objects.count() == 0
