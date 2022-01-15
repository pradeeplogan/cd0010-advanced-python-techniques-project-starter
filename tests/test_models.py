""" Check that an `NearEarthObject` and `CloseApproach` can created and works as intended

To run these tests from the project root, run:

    $ python3 -m unittest tests/test_models.py
"""

import unittest
import math
from models import NearEarthObject



class TestNearEarthObject(unittest.TestCase):
    """ Testing the class NearEarthObject with empty
    and dummy values
    """

    dummy_1 = {'pdes' : '433', 'name' : 'Eros', 'diameter' : 16.840, 'pha' : False}
    dummy_2 = {'pdes' : '486', 'diameter' : 377.78, 'pha' : False}
    dummy_3 = {'pdes' : '687', 'name' : 'Shyam', 'pha' : True}
    dummy_4 = {'pdes' : '687', 'name' : 'Shyam', 'pha' : False}

    def test_empty_neos(self):
        """ TDD """
        neo = NearEarthObject()
        self.assertIsNone(neo.designation)
        self.assertIsNone(neo.name)
        assert(math.isnan(neo.diameter))

    def test_neos_dummy(self):
        """ TDD """
        neo = NearEarthObject(**self.dummy_1)
        self.assertEqual(neo.designation, '433')
        self.assertEqual(neo.name, 'Eros')
        self.assertEqual(neo.diameter, 16.840)
        self.assertEqual(neo.hazardous, False)
        self.assertEqual(neo.fullname, "433 (Eros)")

    def test_neos_no_name(self):
        """ TDD """
        neo = NearEarthObject(**self.dummy_2)
        self.assertEqual(neo.designation, '486')
        self.assertIsNone(neo.name)
        self.assertEqual(neo.diameter, 377.78)
        self.assertEqual(neo.hazardous, False)
        self.assertEqual(neo.fullname, "486")

    def test_neos_no_diameter(self):
        """ TDD """
        neo = NearEarthObject(**self.dummy_3)
        self.assertEqual(neo.designation, '687')
        self.assertEqual(neo.name, 'Shyam')
        assert(math.isnan(neo.diameter))
        self.assertEqual(neo.hazardous, True)
        self.assertEqual(neo.fullname, "687 (Shyam)")

    def test_neos_print_(self):
        """ TDD """
        neo_empty = NearEarthObject()
        self.assertEqual(neo_empty.__str__(), "No matching NEOs exist in the database.")

        neo_dummy1 = NearEarthObject(**self.dummy_1)
        self.assertEqual(neo_dummy1.__str__(), "A NearEarthObject 433 (Eros) \
                         has a diameter of 16.840 km and is not potentially hazardous.")
    
        neo_unknown_diameter = NearEarthObject(**self.dummy_4)
        self.assertEqual(neo_unknown_diameter.__str__(), "A NearEarthObject 687 (Shyam) \
                         has a unknown diameter and is not potentially hazardous.")

        neo_hazard = NearEarthObject(**self.dummy_3)
        self.assertEqual(neo_hazard.__str__(), "A NearEarthObject 687 (Shyam) \
                         has a unknown diameter and is potentially hazardous.")


if __name__ == '__main__':
    unittest.main()
