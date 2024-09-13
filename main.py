"""
Main cli or app entry point
"""
from mylib.calculator import load_dataset, create_histogram, save_to_md


def g_describe():
    g = load_dataset()
    return g.describe()


if __name__ == "__main__":
    df = g_describe()
    print(df)
    create_histogram(df, "id")
    save_to_md()
