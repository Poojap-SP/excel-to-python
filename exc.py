import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
data = pd.read_excel(r'C:\Users\psp91\Downloads\data.xlsx')

# Extract data for plotting
x = data['X values']
y = data['Y values']

# Plot the data
plt.plot(x, y, marker='o')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Line Plot from Excel Data')
plt.grid(True)
plt.show()