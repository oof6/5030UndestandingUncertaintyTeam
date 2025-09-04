# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('metabric.csv')
def outliers(x):
    data = np.array(x)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return (data < lower_bound) | (data > upper_bound)