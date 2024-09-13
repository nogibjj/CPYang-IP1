"""
Main cli or app entry point
"""
from mylib.calculator import *


def g_describe():
    g = load_dataset()
    return g.describe()


if __name__ == "__main__":
    print(g_describe())

