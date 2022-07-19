import unittest, os
from test_functions import test_raining, test_not_raining, test_location, test_env_check

class MyFirstTests(unittest.TestCase):

    def test_raining(self):
        location = "Upper Changi Road North"
        self.assertEqual(test_raining(test_json_file, location), 'Upper Changi Road North, 12:10, 1.8mm, Raining')
    
    def test_not_raining(self):
        location = "Bukit Timah Road"
        self.assertEqual(test_not_raining(test_json_file, location), 'Bukit Timah Road, 12:10, 0mm, Not Raining')
    
    def test_location(self):
        location = "Tuas West Road"
        self.assertEqual(test_location(test_json_file, location), 'S82')

    def test_env_check(self):
        os.environ['LOCATION'] = "Ang Mo Kio Avenue 5"
        self.assertEqual(test_env_check(), 'Ang Mo Kio Avenue 5')

if __name__ == '__main__':
    # Test data file
    test_json_file = "api_raining.json" 
    unittest.main()