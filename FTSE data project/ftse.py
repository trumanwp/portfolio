import pandas as pd

df = pd.read_csv("/Users/adam/repos/portfolio/FTSE data project/data/ftsetimes.csv")
#print(df.to_string())

df.fillna(0, inplace=True) #removing empty cells
print(df.to_string())