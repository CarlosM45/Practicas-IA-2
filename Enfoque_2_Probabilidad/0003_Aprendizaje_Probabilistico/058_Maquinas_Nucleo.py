# Máquinas de vectores soporte (Núcleo)
# Import necessary libraries
from sklearn import svm
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()
# We only take the first two
# features for simplicity
X = iris.data[:, :2]
y = iris.target

# Fit the SVM model
model = svm.SVC(kernel='linear')
model.fit(X, y)
 
# Predict using the SVM model
predictions = model.predict(X)
 
# Evaluate the predictions
accuracy = model.score(X, y)
print("Accuracy of SVM:", accuracy)