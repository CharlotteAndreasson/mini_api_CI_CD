"""
Unit tests for second end-point
"""


import json
from .fixture import client


def test_third_status_code(client):
    """
    Test the api HTTP status code
    :param client: App test client from fixture
    :return: None
    """
    response = client.get('/api/v1.0/third')
    assert response.status_code == 200


def test_third_data(client):
    """
    Test the data from a call to the first end-point
    :param client: App test client from fixture
    :return: None
    """
    response = client.get('/api/v1.0/third')
    data = json.loads(response.text)
    assert data['name'] == 'Charlotte'
