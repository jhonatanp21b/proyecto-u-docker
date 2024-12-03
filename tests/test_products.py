import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_get_products():
    client = APIClient()
    response = client.get(reverse('products'))
    assert response.status_code == 200
