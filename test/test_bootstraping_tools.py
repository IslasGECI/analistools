from bootstraping_tools import *

def test_seasons_from_date():
    input_date=pd.DataFrame(["13/May/2019","16/May/2018","23/Abr/2020","25/Abr/2018"], columns =['Fecha'])
    expected=np.array(["2019","2018","2020","2018"])
    obtained=seasons_from_date(input_date)
    np.testing.assert_array_equal(obtained,expected)