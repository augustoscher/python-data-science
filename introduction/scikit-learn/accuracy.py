from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Loading data
# X is iris.data
# y is iris.target
# X contains the features and y contains the labels
(X, y) = load_iris(return_X_y=True)

# X_train contains the training features
# X_test contains the testing features
# y_train contains the training label
# y_test contains the testing labels
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.5, random_state=42)

classifier = KNeighborsClassifier(n_neighbors=5)

# Train model
classifier.fit(X_train, y_train)

# Prediction
predictions = classifier.predict(X_test)

# Predictions can be matched with the expected output to measure the accuracy value.
print(f'Accuracy Score: {accuracy_score(y_test, predictions)}')

# ---------------------------------------------------------------------

