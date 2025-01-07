# data_analysis_-_visualisation
data analysis techniques and visualization using python 


Iris Dataset Analysis and Visualization
Overview
This Python script is designed to load, explore, analyze, and visualize the Iris dataset using popular data science libraries such as pandas, numpy, matplotlib, and seaborn. It provides insights into the dataset's structure, statistics, and relationships among its features.

Features
Load Data:

Loads the Iris dataset using sklearn.datasets.
Converts numerical species codes into human-readable labels (setosa, versicolor, virginica).
Handles errors during data loading.
Explore Data:

Displays the first few rows of the dataset.
Summarizes dataset structure, data types, and missing values.
Analyze Data:

Provides descriptive statistics for numerical columns.
Calculates mean values for each Iris species.
Visualize Data:

Line plot of average measurements by species.
Bar plot of average sepal length by species.
Histogram of petal length distribution.
Scatter plot of sepal length vs petal length, color-coded by species.
Requirements
Python 3.7 or later
Libraries:
pandas
numpy
matplotlib
seaborn
scikit-learn
To install the required libraries, run:

bash
Copy code
pip install pandas numpy matplotlib seaborn scikit-learn
How to Run
Clone or download the script.
Open a terminal in the directory containing the script.
Run the script using:
bash
Copy code
python script_name.py
Output
The script performs the following:

Displays basic data exploration and statistical analysis in the terminal.
Generates the following visualizations:
Line Plot: Average measurements by species.
Bar Plot: Average sepal length by species.
Histogram: Distribution of petal length.
Scatter Plot: Sepal length vs petal length.
File Structure
load_data(): Loads the Iris dataset and prepares it for analysis.
explore_data(df): Performs data exploration tasks.
analyze_data(df): Conducts statistical analysis.
create_visualizations(df): Generates various plots to visualize the data.
main(): Executes the script's tasks in sequence.
Example Output
Terminal Output:
Basic statistics for the dataset.
Dataset structure and summary.
Visualization:
Multi-panel plots showcasing relationships and distributions in the data.

