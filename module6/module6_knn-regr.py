import numpy as np

# Read user inputs
N = int(input("Enter N (number of points): "))
if N <= 0:
    print("Error: N must be a positive integer.")
    exit()

k = int(input("Enter k (number of neighbors): "))
if k <= 0:
    print("Error: k must be a positive integer.")
    exit()

# Read N (x, y) points
points = []
for i in range(N):
    x, y = map(float, input(f"Enter x and y for point {i+1} (separated by space): ").split())
    points.append((x, y))

# Convert to NumPy arrays
points = np.array(points)
X_train, y_train = points[:, 0], points[:, 1]

# Read the input X value for prediction
X_test = float(input("Enter the X value for prediction: "))

# Validate k
if k > N:
    print("Error: k cannot be greater than N.")
    exit()

# Compute distances and get k nearest neighbors
distances = np.abs(X_train - X_test)
nearest_indices = np.argsort(distances)[:k]  # Get k nearest indices
y_pred = np.mean(y_train[nearest_indices])   # Average of k nearest y-values

# Output result
print(f"Predicted Y value: {y_pred}")
