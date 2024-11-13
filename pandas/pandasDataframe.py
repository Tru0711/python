import pandas as pd

# Create a DataFrame with product data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Price': [150, 200, 300, 250, 400],
    'Quantity': [10, 15, 5, 7, 8]
}
df = pd.DataFrame(data)

# Calculate total price and average price
total_price = df['Price'].sum()
average_price = df['Price'].mean()

print("Product Data:")
print(df)
print("\nTotal Price:", total_price)
print("Average Price:", average_price)
