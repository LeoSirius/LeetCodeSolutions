import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)