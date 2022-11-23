https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#### DO NOT CHANGE THE BELOW CODE ####

from sklearn.datasets import load_diabetes
from sklearn.datasets import load_linnerud
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
import numpy as np

features, target_vals = load_diabetes(return_X_y = True)

num_data, num_features = features.shape

# Append a value of 1 to each data point feature vector so we fit the intercept and increment num features
features = np.insert(features, num_features, 1, axis=1)
num_features += 1 

features, target_vals = shuffle(features, target_vals, random_state=1)

#### DO NOT CHANGE THE ABOVE CODE ####

# This holds the average error rate on the test folds for each value of lambda
lambda_val_rmse = []

for lambda_val in [0.1, 1, 10, 100]:

    k_fold = KFold(n_splits=5)

    # This holds the error rates on each of the 5 test folds for a specific value of k
    rmse_vals = []

    for train_idx, test_idx in k_fold.split(features):

        train_features = features[train_idx]
        train_target_vals = target_vals[train_idx]
        test_features = features[test_idx]
        test_target_vals = target_vals[test_idx]

        #### ADD YOUR CODE HERE ####


    lambda_val_rmse.append(np.average(rmse_vals))

print('Average test RMSE for each value of lambda:', lambda_val_rmse)
