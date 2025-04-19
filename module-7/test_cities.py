# test_cities.py

import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the function format_city_country()."""

    def test_city_country(self):
        """Do city and country like 'Santiago, Chile' work?"""
        result = format_city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()
