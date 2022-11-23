https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#### DO NOT CHANGE THE BELOW CODE ####

from sklearn.datasets import load_wine
from sklearn.utils import shuffle
import numpy as np

percent_train = 0.8

num_reps = 10

features, labels = load_wine(return_X_y = True)

class_0 = 0
class_1 = 1

features = features[(labels == class_0) | (labels == class_1)]
labels = labels[(labels == class_0) | (labels == class_1)]

num_data, num_features = features.shape
split = int(np.ceil(num_data*percent_train))

features, labels = shuffle(features, labels, random_state=1)

train_features, train_labels = (features[:split], labels[:split])
test_features, test_labels = (features[split:], labels[split:])

num_train_data = train_features.shape[0]
num_test_data = test_features.shape[0]

#### DO NOT CHANGE THE ABOVE CODE ####

# Use this to store your error rates for each repetition
error_rates = []

for repetition in range(num_reps):

    #### ADD YOUR CODE HERE ####


print('Average error rate:', np.average(error_rates))
print('Error rate standard deviation:', np.std(error_rates))
