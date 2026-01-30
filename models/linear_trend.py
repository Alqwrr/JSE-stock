import numpy as np
from sklearn.linear_model import LinearRegression

def estimate_trend(prices: list[float]) -> float:
    X = np.arange(len(prices)).reshape(-1, 1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(X, y)

    return model.coef_[0]
