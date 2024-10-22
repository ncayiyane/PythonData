import pandas as pd # Import pandas for data analysis and manipulation
import numpy as np # Import numpy for numerical computing. Numpy provides support for arrays and matrices.
import matplotlib.pyplot as plt # Imports matplotlib.pyplot as plt. This is a plotting library used for creating static, interactive, and animated visualizations in Python. 
import seaborn as sns # Imports seaborn as sns. Seaborn is a Python data visualization library based on matplotlib.

# Load the dataset
df = pd.read_csv('Marvel Movies.csv') # Read the CSV file into a pandas DataFrame. The data will be loaded for analysis and manipulation.

# Print the first 10 rows
print(df.head(10)) # Print the first 10 rows of the DataFrame.

print(df.describe()) # Displays summary statistics (like mean, median, standard deviation, etc.) for each column in the DataFrame.

print(df.isnull().sum()) # Displays the number of missing values in each column.
 
print(df.dtypes) # Displays the data types of each column in the DataFrame.

# print(df.shape)
df = df.drop_duplicates() # Remove duplicate rows

# Convert percentage columns to numeric values after removing the '%' symbol
percentage_columns = ['% budget recovered', 'critics % score', 'audience % score', 'audience vs critics % deviance'] # Define the percentage columns to convert
for column in percentage_columns:
    df[column] = df[column].str.rstrip('%').astype(float) # Remove the '%' symbol and convert to float

# Display the updated data types to ensure they are appropriate
print("\nData types after cleaning:")
print(df.dtypes) #

# Descriptive statistics
print("\nDescriptive statistics for numerical columns:") 
print(df.describe()) # Displays summary statistics (like mean, median, standard deviation, etc.) for each column in the DataFrame.

# Histogram of Worldwide Gross Revenue
plt.figure(figsize=(8, 5)) # Set the figure size
sns.histplot(df['worldwide gross ($m)'], bins=10, kde=True) # Create the histogram
plt.title('Distribution of Worldwide Gross Revenue') # Set the title
plt.xlabel('Worldwide Gross ($m)') # Set the x-axis label
plt.ylabel('Frequency') # Set the y-axis label
plt.show() # Display the histogram

# Scatter plot of Budget vs. Worldwide Gross Revenue
plt.figure(figsize=(8, 5)) # Set the figure size
sns.scatterplot(data=df, x='budget', y='worldwide gross ($m)') # Create the scatter plot
plt.title('Budget vs. Worldwide Gross Revenue') # Set the title
plt.xlabel('Budget ($m)') # Set the x-axis label
plt.ylabel('Worldwide Gross ($m)') # Set the y-axis label
plt.show() # Display the scatter plot


# Reshape the DataFrame to make it easier to plot side by side
df_melted = df.melt(id_vars='movie', value_vars=['audience % score', 'critics % score'],
                    var_name='Score Type', value_name='Score')

plt.figure(figsize=(14, 8))

# Create a barplot with hue to show audience and critics scores side by side
sns.barplot(data=df_melted, x='movie', y='Score', hue='Score Type', width=0.8 )

plt.xticks(rotation=90)
plt.title('Audience vs Critics Scores for Marvel Movies')
plt.xlabel('Movie')
plt.ylabel('Score (%)')
plt.legend(title='Score Type')
plt.show()

# plt.figure(figsize=(14, 8))
# df['movie'] = df['movie'].astype(str)
# sns.barplot(data=df, x='movie', y='audience % score', color='green', label='Audience Score')
# sns.barplot(data=df, x='movie', y='critics % score', color='pink', label='Critics Score', alpha=0.6)
# plt.xticks(rotation=90)
# plt.title('Audience vs Critics Scores for Marvel Movies')
# plt.xlabel('Movie')
# plt.ylabel('Score (%)')
# plt.legend()
# plt.show()

# Correlation matrix to understand relationships between different numeric variables
# correlation_matrix = df.corr()
# print("\nCorrelation matrix:")
# print(correlation_matrix)

# # Visualize the correlation matrix
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()

# # Bar plot comparing audience scores vs critics scores for each movie




# plt.figure(figsize=(14, 8))
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()
