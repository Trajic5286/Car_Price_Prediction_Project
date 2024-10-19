import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = 'data/car_prices.csv'
df = pd.read_csv(file_path)


# Show initial information about the data
print("First 5 rows of the dataset:")
print(df.head())

df = pd.get_dummies(df, columns=['Make', 'Model', 'Color'])
df['Price'] = df['Price'].astype(float)
df['Mileage'] = df['Mileage'].astype(float)


print("\nDataset Information:")
df.info()

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Descriptive statistics
print("\nSummary Statistics:")
print(df.describe())

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Features')
plt.show()
