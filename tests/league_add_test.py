import unittest
import azure.functions as func 

from LeagueAdd import main
from unittest import mock 

class TestLeagueAdd(unittest.TestCase):
    def test_league_add_success(self):
        assert True == True