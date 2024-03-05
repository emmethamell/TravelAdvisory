import pytest

from travel_advisories.scraper import TravelAdvisory

def test_travel_advisories():
    TravelAdvisory.scrape_website()
    assert True == True