import unittest
import azure.functions as func 
import json

from LeagueAdd import main
from unittest import mock 

class TestLeagueAdd(unittest.TestCase):
    def test_league_add_success(self):
        # Request 
        request = func.HttpRequest(
            method='POST',
            url='api/leagues/create',
            body=json.dumps({
                'name': 'Foobar',
                'country': 'can'
            }).encode('utf8')
        )

        response = main(request)

        # Assertions
        assert response.status_code == 200
        assert "League successfully created. Name : Foobar, country : can." in response.get_body().decode()