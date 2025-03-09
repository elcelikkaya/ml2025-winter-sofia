import numpy as np
from sklearn.metrics import precision_score, recall_score

# Step 1: Ask for the number of points
N = int(input("Enter the number of (x, y) points: "))

# Step 2: Initialize arrays
x_values = np.zeros(N, dtype=int)  # Ground truth (actual classes)
y_values = np.zeros(N, dtype=int)  # Predicted classes

# Step 3: Get user input
print("Enter values for x (ground truth) and y (predicted), both 0 or 1:")
for i in range(N):
    x_values[i] = int(input(f"Enter x[{i+1}]: "))
    y_values[i] = int(input(f"Enter y[{i+1}]: "))

# Step 4: Compute precision and recall
precision = precision_score(x_values, y_values)
recall = recall_score(x_values, y_values)

# Step 5: Print results
print("\nResults:")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
