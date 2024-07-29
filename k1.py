import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
data = pd.read_excel(r'C:\Users\psp91\Downloads\Amazon 1_Raw.xlsx')

# Extract data for plotting
x = data['Sales']
y = data['Profit']

# Plot the data
plt.plot(x, y, marker='o')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Line Plot from Excel Data')
plt.grid(True)
plt.show()

