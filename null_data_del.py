import pandas as pd

# df = pd.read_ . . .
# ------------------------- read data and save in df
# after

null_count = df.isnull().sum()
null_count = null_count.reset_idex()
null_count.columns = ['collist', 'value']
null_count.sort_values(by='value', ascending=False).head() # head value it can change
null_count['collist'].tolist() # or .values
df = df.drop(null_count, axis=1)
