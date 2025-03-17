import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Function to read input data
def read_data():
    N = int(input("Enter the number of training samples (N): "))
    train_data = np.zeros((N, 2))
    
    print("Enter the training samples (x y):")
    for i in range(N):
        x, y = map(float, input().split())
        train_data[i] = [x, y]
    
    M = int(input("Enter the number of test samples (M): "))
    test_data = np.zeros((M, 2))
    
    print("Enter the test samples (x y):")
    for i in range(M):
        x, y = map(float, input().split())
        test_data[i] = [x, y]
    
    return train_data, test_data

# Load data
train_data, test_data = read_data()

# Splitting features (X) and labels (Y)
X_train, y_train = train_data[:, 0].reshape(-1, 1), train_data[:, 1].astype(int)
X_test, y_test = test_data[:, 0].reshape(-1, 1), test_data[:, 1].astype(int)

# Define the kNN model and hyperparameter grid
knn = KNeighborsClassifier()
param_grid = {'n_neighbors': np.arange(1, 11)}

grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get the best k
best_k = grid_search.best_params_['n_neighbors']

# Train the best model
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train, y_train)

# Predict on test set
y_pred = best_knn.predict(X_test)

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)

# Output results
print(f"Best k: {best_k}")
print(f"Test accuracy: {accuracy:.4f}")
