import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
try:
    data_frame=pd.read_csv('data_sets/data.csv')
except Exception as e:
    print(e)
print(data_frame.shape)