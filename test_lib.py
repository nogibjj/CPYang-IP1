from mylib.calculator import grab_mean, load_dataset


def test_libs():
    df = load_dataset()
    assert grab_mean(df, "id") > 0
