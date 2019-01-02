Your task this week is to implement a multiclass perceptron.

Our goal is for our program to recognize images of handwritten digits as well as to identify Iris flower species based on some specific measurements.

Your task is to complete the implementation of the multiclass perceptron in the Python module perceptron.py by filling in the code for the two methods:

1. predict: Predict the label of a given example represented by a feature vector. That label can be a digit (0-9 for the handwritten digits dataset), a species ('Iris-virginica', 'Iris, versicolor', 'Iris, virginica' for the Iris dataset) or some other label for some other classification problem.

2. update_weights: Update the Perceptron weights based on a single training example The methods __init__, init_weights and train in the Perceptron class have been implemented for you.

The code that preprocesses the data and creates the feature vectors has also been implemented for you (in classify.py, digits.py and iris.py).

A Vector class implementation is provided in vectors.py that defines the functionality of +, - and * as the addition, subtraction and dot product of two (feature) Vector objects.

Once you implement the predict and update_weights methods, you can run the classifier as follows:

python classifier.py digits This will train the perceptron on the handwritten digits dataset with **default values** for the number of iterations

(2), the number of training examples (3000), the number of validation examples (1000) and the number of test examples (1000).

The validation output is saved in 'digit_validation_output.txt'.

The test output is saved in 'digit_test_output.txt'

To train the perceptron with 4 iterations on the digits dataset using only 1500 training examples and 500 examples for validation and test, you can type:

	python classifier.py digits 4 1500 500 500

To train the perceptron with 6 iterations on the Iris dataset using all the examples:

	python classifier.py iris 6
The validation output is saved in 'iris_validation_output.txt'.

The test output is saved in 'iris_test_output.txt'