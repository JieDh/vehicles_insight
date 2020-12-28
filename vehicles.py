import pandas as pd
def df_shape(x):
    return x.shape
vehicles = pd.read_csv('data/vehicles.csv', sep=',')
print(df_shape(vehicles))
