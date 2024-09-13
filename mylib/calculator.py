"""
Calculations library
"""
import pandas as pd
import matplotlib.pyplot as plt 


path = "train.csv"

df = pd.read_csv(path)

def load_dataset():
    df = pd.read_csv(path)
    return df

def grab_mean(df, col):
    return df[col].mean()

def create_histogram(df, col):
    
    # Plotting a basic histogram
    plt.hist(df[col],  color='skyblue', edgecolor='black')
    
    # Adding labels and title
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title('Histogram of {}'.format(col))
    plt.savefig("lol.png")
    
def grab_median(df, col):
    return df[col].median()

def grab_STD(df, col):
    return df.describe()['col']['std']

def grab_max(df, col):
    return max(df[col])

def save_to_md():
    with open("test.md", "a") as file:
        file.write("test")
        



