import unittest
import numpy as np
from bootstraping_tools import *

def test_seasons_from_date():
    input_date=pd.DataFrame(["13/May/2019","16/May/2018","23/Abr/2020","25/Abr/2018"], columns =['Fecha'])
    expected=np.array(["2019","2018","2020","2018"])
    obtained=seasons_from_date(input_date)
    np.testing.assert_array_equal(obtained,expected)

class TestAnalistools(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        self.T: int = 1
        self.Lambda = 2
        self.No: int = 1
        self.data_original: np.array = np.array([1, 1, 1, 1, 1, 1, 2])

    def test_power_law(self):
        output = power_law(self.T, self.Lambda, self.No)
        self.assertEqual(output, 2)

    def test_remove_distribution_outliers(self):
        output = remove_distribution_outliers(self.data_original)
        self.assertTrue((output == self.data_original).all())

    def test_boostrapping_feature(self):
        output = boostrapping_feature(self.data_original, N = 2)
        self.assertEqual(output, [2, 2])

if __name__ == "__main__":
    unittest.main()