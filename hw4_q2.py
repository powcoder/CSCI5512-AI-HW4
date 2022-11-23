https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#### DO NOT CHANGE THE BELOW CODE ####

from sklearn.datasets import load_wine
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
import numpy as np

features, labels = load_wine(return_X_y = True)

class_0 = 0
class_1 = 1

features = features[(labels == class_0) | (labels == class_1)]
labels = labels[(labels == class_0) | (labels == class_1)]

num_data, num_features = features.shape

features, labels = shuffle(features, labels, random_state=1)

#### DO NOT CHANGE THE ABOVE CODE ####

# This holds the average error rate on the test folds for each value of k
k_error_rates = []

for k in [23, 51, 101]:

    k_fold = KFold(n_splits=5)

     # This holds the error rates on each of the 5 test folds for a specific value of k
    error_rates = []

    for train_idx, test_idx in k_fold.split(features):

        train_features = features[train_idx]
        train_labels = labels[train_idx]
        test_features = features[test_idx]
        test_labels = labels[test_idx]

        #### ADD YOUR CODE HERE ####


    k_error_rates.append(np.average(error_rates))

print('Average test error for each value of k:', k_error_rates)
