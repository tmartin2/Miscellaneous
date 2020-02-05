"""Logistic Regression

Author: Trevor Martin
Date: 19 January 2020
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def main():
    
    # "x" variable
    # x = np.array([5, 15, 25, 35, 45, 55]) # (6,)
    regressors = np.array([3, 3, 5, 6, 2, 10,
                           11, 3, 5, 6, 7, 8,
                           9, 3, 2, 2, 2, 2]).reshape((-1, 1)) # (18, 1)
    # = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    # = np.matrix([5, 15, 25, 35, 45, 55]).T # (6, 1)
    # = np.array([5, 15, 25, 35, 45, 55])[:, np.newaxis] # (6, 1)
    
    # "y" variable
    predictors = np.array([1, 2, 4, 3, 1, 6,
                           6, 1, 2, 5, 4, 4,
                           4, 4, 1, 1, 2, 1])

    logistic_model = LogisticRegression()
    logistic_model.fit(regressors, predictors)

    coeff_det = logistic_model.score(regressors, predictors) # coefficient of determination

    predictions = logistic_model.predict(regressors)

    confus_matrix = confusion_matrix(predictors, predictions)
    print(f"{confus_matrix}")
    report = classification_report(predictors, predictions)
    print(f"{report}")

if __name__ == '__main__':
    main()
