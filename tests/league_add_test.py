import unittest
import azure.functions as func 
import json

from LeagueAdd import main
from unittest import mock 

class TestLeagueAdd(unittest.TestCase):
    def test_league_add_200(self):
        # Setup
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

    def test_league_add_422(self):
        # Setup 
        request = func.HttpRequest(
            method='POST',
            url='api/leagues/create',
            body=json.dumps({}).encode('utf8')
        )

        response = main(request)

        # Assertions
        assert response.status_code == 422
        assert "Params are missing. Please include at least a 'name' to create a league." in response.get_body().decode()
