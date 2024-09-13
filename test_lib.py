from mylib.calculator import *

def test_libs():
    df = load_dataset()
    assert grab_mean(df, 'id') > 0