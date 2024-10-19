import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your dataset (make sure this path is correct)
 # Change to your actual data file

# Call the functions to plot # Replace with the actual feature name


def plot_price_distribution(df):
    """Plots the distribution of car prices"""
    plt.figure(figsize=(10,6))
    sns.histplot(df['Price'], kde=True, bins=30)
    plt.title('Car Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

def plot_feature_relationship(df, feature):
    """Plots the relationship between a given feature and price"""
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=df[feature], y=df['Price'])
    plt.title(f'Relationship between {feature} and Price')
    plt.xlabel(feature)
    plt.ylabel('Price')
    plt.show()




df = pd.read_csv('data/car_prices.csv') 

print(df.columns)

plot_price_distribution(df)

plot_feature_relationship(df, 'Year')  # Example for year
plot_feature_relationship(df, 'Mileage')
plot_feature_relationship(df, 'Color')  # Example for mileage
