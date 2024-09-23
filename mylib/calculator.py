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
    plt.figure(figsize=(10, 6))
    # Plotting a basic histogram
    plt.hist(df[col], bins=20,  color='skyblue', edgecolor='black')
    
    # Adding labels and title
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title('Histogram of {}'.format(col))
    plt.grid(axis='y', alpha=0.75)
    plt.savefig("hist_{}.png".format(col))
    
def grab_median(df, col):
    return df[col].median()

def grab_STD(df, col):
    return df.describe()['col']['std']

def grab_max(df, col):
    return max(df[col])





