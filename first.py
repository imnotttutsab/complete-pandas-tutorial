import pandas as pd

# #Think of Series as a single column
# #Think of DataFrame as a table with multiple columns (rows and columns)
# df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['A', 'B', 'C'], index=['x','y','z'])

# # show the first 3 rows — print so the script outputs to the console
# print(df.head(1))
# print(df.tail(2))
# print(df.info())
# print(df.nunique())
# print(df.shape)  














# #LOading data from CSV file

# coffee = pd.read_csv('./warmup-data/coffee.csv') #you can also provide a csv url instead of file path
# print(coffee.head())      #the use of head() is optional but good for checking if the data is loaded correctly
 

# results = pd.read_parquet('./data/results.parquet')
# print(results.head())


# olympics_data = pd.read_excel('./data/olympics-data.xlsx')
# print(olympics_data.head())












#### FOR DATA SAMPLING AND SPECIFIC DATA  w/ sample, loc(), iloc()

coffee = pd.read_csv("./warmup-data/coffee.csv")
# coffee.index = coffee["Day"]
# print(coffee.sample(4))

# print(coffee.loc["Monday":"Wednesday"])
# print(coffee.loc[6:9, ["Day", "Units Sold"]])

# print(coffee.iloc[:3, [2]])

# coffee.loc[1:3, "Units Sold"] = 10
# print(coffee.loc[1]) 









