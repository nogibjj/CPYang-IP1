"""
Main cli or app entry point
"""
from mylib.calculator import *


def g_describe():
    g = load_dataset()
    return g.describe()

def sate_to_md():
    with open("test.md", "a") as file:
        file.write("test")

if __name__ == "__main__":
    df = g_describe()
    print(df)
    create_histogram(df, 'id')
    
    save_to_md()
    
    

  