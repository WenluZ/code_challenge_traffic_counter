# Test Modul for main.py

import unittest
import unittest.mock

import io
import sys 
sys.path.append('..')

from main.main import sum_count
from main.main import sum_per_day
from main.main import top3_half_hrs
from main.main import period_with_least_cars
from testcase import create_df

df = create_df()

class TestMain(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_sum_count(self, mock_stdout):
        sum_count(df,'count')
        self.assertEqual(mock_stdout.getvalue(), '30\n')

    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_sum_per_day(self, mock_stdout):
        sum_per_day(df,'timestamp','count')
        self.assertEqual(mock_stdout.getvalue(), '2021-12-05 5\n2021-12-08 25\n')


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_top3_half_hrs(self, mock_stdout):
        top3_half_hrs(df,'timestamp','count')
        self.assertEqual(mock_stdout.getvalue(), '2021-12-08 19:00:00 15\n2021-12-08 18:00:00 10\n2021-12-05 15:30:00 5\n')
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_period_with_least_cars(self, mock_stdout):
        period_with_least_cars(df,'timestamp')
        self.assertEqual(mock_stdout.getvalue(), 'The 1.5 hour period after the below times with least cars\n2021-12-08 17:00:00 15.0\n')



if __name__ == "__main__":
    unittest.main()