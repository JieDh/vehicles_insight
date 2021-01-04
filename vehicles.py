import pandas as pd
def df_shape(x):
    return x.shape
vehicles = pd.read_csv('data/vehicles.csv', sep=',')
print("Dataframe shape:", df_shape(vehicles))

def df_rows(x):
        return len(x)
print("Dataframe rows:", df_rows(vehicles))

def df_cols(x):
        return len(x.columns)
print("Dataframe columns:", df_cols(vehicles))

def df_col_name(x):
	return x.columns.to_list()
print("Column names:", df_col_name(vehicles))

