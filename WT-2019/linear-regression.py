"""Linear Regression

Author: Trevor Martin
Date: 19 January 2020
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


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

    linear_model = LinearRegression()
    linear_model.fit(regressors, predictors)

    coeff_det = linear_model.score(regressors, predictors) # coefficient of determination
    # linear_model.intercept_ gets model intercept
    # linear_model.coef_ gets slope
    
    predictions = linear_model.predict(regressors)
    # or linear_model.intercept_ + model.coef_ * regressors
    
    plt.scatter(regressors, predictors, color="blue")
    plt.plot(regressors, predictions, color="red", linewidth=3)
    plt.show()    

if __name__ == '__main__':
    main()
