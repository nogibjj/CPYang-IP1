"""
Main cli or app entry point
"""
from mylib.calculator import load_dataset, create_histogram


def g_describe():
    g = load_dataset()
    return g.describe()


def save_to_md():

    sample_string = """
    # This is a sample report 
    
    ## Behold, analysis
    
    We can see the distribution of id's in the housing data
    ![Figure](hist_id.png)

    There's also a histogram of the age of the houses.

    ![Age Histogram](hist_HouseAge.png)

    And a histogram of the population of the cities of the houses.

    ![Age Histogram](hist_Population.png)
    """
    with open("test.md", "w") as file:
        file.write(sample_string)


if __name__ == "__main__":
    df = load_dataset()
    print(g_describe())
    create_histogram(df, "id")
    create_histogram(df, "HouseAge")
    create_histogram(df, "Population")
    save_to_md()
