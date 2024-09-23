"""
Main cli or app entry point
"""
from mylib.calculator import load_dataset, create_histogram


def g_describe():
    g = load_dataset()
    return g.describe()


def save_to_md():
    with open("test.md", "w") as file:
        file.write("# This is a sample report \n ")
        file.write("![Figure](hist.png)")


if __name__ == "__main__":
    df = g_describe()
    print(df)
    create_histogram(df, "id")
    create_histogram(df, "HouseAge")
    create_histogram(df, "Population")
    save_to_md()
