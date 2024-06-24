import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Datasets
police_shootings = pd.read_csv('police_shooting.csv', parse_dates=['date'])
census_data = pd.read_csv('census_data.csv')

# Step 2: Verify Column Names (optional)
# print("Police Shootings Columns:", police_shootings.columns)
# print("Census Data Columns:", census_data.columns)

# Step 3: Merge Datasets
# Assuming the state column exists in both datasets based on your description
merged_data = pd.merge(police_shootings, census_data, left_on='state', right_on='Geographic Area Name (NAME)', how='left')

# Step 4: Exploratory Data Analysis (EDA)

# Example EDA: Analyze incidents by race
race_counts = merged_data['race'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=race_counts.index, y=race_counts.values)
plt.title('Police Shootings by Race')
plt.xlabel('Race')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('police_shootings_by_race.png')
plt.show()

# Example EDA: Compare incidents by gender (adjust based on actual columns available)
if 'gender' in merged_data.columns:
    gender_counts = merged_data['gender'].value_counts()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=gender_counts.index, y=gender_counts.values)
    plt.title('Police Shootings by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Incidents')
    plt.tight_layout()
    plt.savefig('police_shootings_by_gender.png')
    plt.show()
else:
    print("'gender' column not found in merged dataset. Adjust visualization code accordingly.")

# Additional EDA: Correlation between numeric columns
# Identify numeric columns for correlation
numeric_columns = merged_data.select_dtypes(include=['int64', 'float64']).columns

# Compute correlation matrix for numeric columns
correlation_matrix = merged_data[numeric_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.show()
