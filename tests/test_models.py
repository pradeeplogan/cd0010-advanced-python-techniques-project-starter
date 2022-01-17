""" Check that an `NearEarthObject` and `CloseApproach` can created and works as intended

To run these tests from the project root, run:

    $ python3 -m unittest tests/test_models.py
"""

import unittest
import math
import datetime
from models import CloseApproach, NearEarthObject



class TestNearEarthObject(unittest.TestCase):
    """ Testing the class NearEarthObject with empty
    and dummy values
    """

    dummy_1 = {'pdes' : '433', 'name' : 'Eros', 'diameter' : 16.840, 'pha' : False}
    dummy_2 = {'pdes' : '486', 'diameter' : 377.78, 'pha' : False}
    dummy_3 = {'pdes' : '687', 'name' : 'Shyam', 'pha' : True}
    dummy_4 = {'pdes' : '687', 'name' : 'Shyam', 'pha' : False}

    close_approch_dummy_1 = {'des' : "170903", "cd" : "1900-Jan-01 00:11", "dict" : 0.0921795123769547, "v_rev" : 16.7523040362574}





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
        self.assertEqual(neo_dummy1.__str__(), "A NearEarthObject 433 (Eros) "\
                         "has a diameter of 16.840 km and is not potentially hazardous.")

        neo_unknown_diameter = NearEarthObject(**self.dummy_4)
        self.assertEqual(neo_unknown_diameter.__str__(), "A NearEarthObject 687 (Shyam) "\
                         "has a unknown diameter and is not potentially hazardous.")

        neo_hazard = NearEarthObject(**self.dummy_3)
        self.assertEqual(neo_hazard.__str__(), "A NearEarthObject 687 (Shyam) "\
                         "has a unknown diameter and is potentially hazardous.")

    def test_close_approch_empty(self):
        """ TDD """
        cls_app = CloseApproach()
        self.assertIsNone(cls_app._designation)
        self.assertIsNone(cls_app.time)
        assert(math.isnan(cls_app.distance))
        assert(math.isnan(cls_app.velocity))

    def test_close_approch_dummy(self):
        """ TDD """
        cls_app = CloseApproach(**self.close_approch_dummy_1)
        self.assertEqual(cls_app._designation, "170903")
        self.assertEqual(cls_app.time, datetime.datetime(1900, 1, 1, 0, 11))
        self.assertEqual(cls_app.distance, 0.0921795123769547)
        self.assertEqual(cls_app.velocity, 16.7523040362574)

    def test_close_approch_str(self):
        """ TDD """
        neo_obj = NearEarthObject(**self.dummy_1)
        new_dict = self.close_approch_dummy_1
        new_dict.update({"neo" : neo_obj})
        cls_app = CloseApproach(**new_dict)
        self.assertEqual(cls_app.fullname, "433 (Eros)")
        self.assertEqual(cls_app.__str__(), "On 1900-01-01 00:11, '433 (Eros)' approaches " \
                         "Earth at a distance of 0.09 au and a velocity of 16.75 km/s.")

        
if __name__ == '__main__':
    unittest.main()
