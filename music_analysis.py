import pandas as pd  # Import pandas for data analysis and manipulation
import numpy as np  # Import numpy for numerical computing
import matplotlib.pyplot as plt  # Import for creating visualizations
import seaborn as sns  # Import seaborn for enhanced visualizations

# Load the dataset
df = pd.read_csv('Marvel Movies.csv')  # Read the CSV file into a pandas DataFrame

# Initial data exploration
print("First 10 rows of the dataset:")
print(df.head(10))  # Display the first 10 rows

print("\nSummary statistics:")
print(df.describe())  # Summary statistics for numerical columns

print("\nMissing values in each column:")
print(df.isnull().sum())  # Check for missing values

print("\nData types of each column:")
print(df.dtypes)  # Check data types of each column

# Data cleaning
df = df.drop_duplicates()  # Remove duplicate rows

# Convert percentage columns to numeric values after removing the '%' symbol
percentage_columns = ['% budget recovered', 'critics % score', 'audience % score', 'audience vs critics % deviance']
for column in percentage_columns:
    df[column] = df[column].str.rstrip('%').astype(float)  # Convert percentage columns to float

print("\nData types after cleaning:")
print(df.dtypes)  # Display data types after cleaning

# Descriptive statistics after cleaning
print("\nDescriptive statistics for numerical columns:")
print(df.describe())  # Summary statistics for numerical columns

# Visualization 1: Histogram of Worldwide Gross Revenue
plt.figure(figsize=(8, 5))
sns.histplot(df['worldwide gross ($m)'], bins=10, kde=True)  # Create histogram
plt.title('Distribution of Worldwide Gross Revenue')
plt.xlabel('Worldwide Gross ($m)')
plt.ylabel('Frequency')
plt.show()

# Visualization 2: Scatter plot of Budget vs. Worldwide Gross Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='budget', y='worldwide gross ($m)')  # Scatter plot of budget vs. revenue
plt.title('Budget vs. Worldwide Gross Revenue')
plt.xlabel('Budget ($m)')
plt.ylabel('Worldwide Gross ($m)')
plt.show()

# Visualization 3: Audience vs Critics Scores Comparison (Bar Plot)
df_melted = df.melt(id_vars='movie', value_vars=['audience % score', 'critics % score'],
                    var_name='Score Type', value_name='Score')  # Reshape the DataFrame for easier plotting

plt.figure(figsize=(14, 8))
sns.barplot(data=df_melted, x='movie', y='Score', hue='Score Type', width=0.8)  # Bar plot for audience vs critics scores
plt.xticks(rotation=90)
plt.title('Audience vs Critics Scores for Marvel Movies')
plt.xlabel('Movie')
plt.ylabel('Score (%)')
plt.legend(title='Score Type')
plt.show()

# New Feature: Display Movies with High Revenue (Sorted by Worldwide Gross)
# Sort the DataFrame by 'worldwide gross ($m)' in descending order
df_sorted = df[['movie', 'budget', 'worldwide gross ($m)']].sort_values(by='worldwide gross ($m)', ascending=False)

# Display the top movies with the highest gross revenue
print("\nMovies sorted by Worldwide Gross Revenue (Highest to Lowest):")
print(df_sorted)
