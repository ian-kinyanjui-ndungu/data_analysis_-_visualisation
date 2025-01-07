import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error handling in the loading of data
def load_data():
    try:
        # Loading iris dataset from sklearn
        iris = load_iris()
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], 
                         columns=['sepal_length', 'sepal_width', 
                                'petal_length', 'petal_width', 'species'])
        # Convert numeric int variables to string labels
        df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

#data exploration
def explore_data(df):
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

#statistical analysis
def analyze_data(df):
    print("Basic Statistics:")
    print(df.describe())
    print("\nMean values by species:")
    print(df.groupby('species').mean())

#visualizations
def create_visualizations(df):
    #plotting style
    plt.style.use('seaborn')
    
    #figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Line plot
    df.groupby('species').mean().plot(marker='o', ax=axes[0,0])
    axes[0,0].set_title('Average Measurements by Species')
    axes[0,0].set_ylabel('Measurement (cm)')
    
    # Bar plot
    df.groupby('species')['sepal_length'].mean().plot(kind='bar', ax=axes[0,1])
    axes[0,1].set_title('Average Sepal Length by Species')
    axes[0,1].set_ylabel('Sepal Length (cm)')
    
    #  Histogram
    df['petal_length'].hist(bins=20, ax=axes[1,0])
    axes[1,0].set_title('Distribution of Petal Length')
    axes[1,0].set_xlabel('Petal Length (cm)')
    axes[1,0].set_ylabel('Frequency')
    
    #Scatter plot
    sns.scatterplot(data=df, x='sepal_length', y='petal_length', 
                    hue='species', ax=axes[1,1])
    axes[1,1].set_title('Sepal Length vs Petal Length')
    
    plt.tight_layout()
    plt.show()

# Main execution
def main():
    # Load the data
    df = load_data()
    if df is None:
        return
    
    # Exploring dataset
    explore_data(df)
    
    #Analyzing data
    analyze_data(df)
    
    # Creating visualizations
    create_visualizations(df)

if __name__ == "__main__":
    main()