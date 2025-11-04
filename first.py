import pandas as pd
import numpy as np

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

#coffee = pd.read_csv("./warmup-data/coffee.csv")
# coffee.index = coffee["Day"]
# print(coffee.sample(4))

# print(coffee.loc["Monday":"Wednesday"])
# print(coffee.loc[6:9, ["Day", "Units Sold"]])

# print(coffee.iloc[:3, [2]])

# coffee.loc[1:3, "Units Sold"] = 10
# print(coffee.loc[1]) 

# coffee.at[0, "Units Sold"] = 15
# print(coffee.at[0, "Units Sold"])



















### ACCESSING DATA && ITERATING DFRAME USING FOR
# print(coffee["Units Sold"])   #accessing a single column
# print(coffee.Day)   #accessing a single column using attribute style access
# print(coffee.sort_values("Units Sold"))
# print(coffee.sort_values(["Units Sold","Coffee Type"], ascending=[1,0]))   #sorting values based on a column

# for index, row in coffee.iterrows():
#     print(index)
#     print(row)





















#### FILTERING DATA


bios = pd.read_csv("./data/bios.csv")
# print(bios.head)
# print(bios.info())

# print(bios.loc[bios['height_cm']>215, ['name','NOC', 'born_country']])

# print(bios[(bios['height_cm']>215) & (bios['born_country']=='USA')])

# print(bios[bios['name'].str.contains('Keith')])  #filtering based on string contains
# print(bios[bios['name'].str.contains('Keith|Patrick')])  #filtering based on multiple string contains using regex OR operator |

# print(bios.query('born_country == "USA" and born_city == "New York"'))  #using query method to filter data see how we use and keyword instead of & operator and also "" inside single quotes ''


























#### ADDING COLUMNS && DROPPING COLUMNS/ROWS And Saving them


# coffee = pd.read_csv("./warmup-data/coffee.csv")

# coffee_new = coffee #if we do this it just points to the smae memory
# coffee_the_return_of_the_bean = coffee.copy() #if we do this then we can create a seperate copy of coffee
# coffee['price'] = np.where(coffee['Coffee Type']=='Espresso',3.99,5.99) #np.where is a numpy syntax taht iterates over the dataframe and runs certain task based on conditional (think of it as if else)
# #the way to add new column is {{dataframe["column"] = "Value"}}
# # print(coffee.head())
# print(coffee_new.head())
# print(coffee_the_return_of_the_bean.head())


# coffee.drop(columns=['price'], inplace=True) #we need to specify "columns=" or else it will think of a index and inPlace makes sure that the drops is saved in the dataframe

# coffee['revenue'] = coffee["Units Sold"] * coffee['price']
# coffee.rename(columns={'price':'Price','revenue':'Revenue'}, inplace=True)
# print(coffee.head())


bios_new = bios.copy()
bios_new['first_name']= bios_new['name'].str.split(' ').str[0]
bios_new.index = bios['athlete_id']
bios_new.drop(columns='athlete_id', inplace=True)
bios_new['dob'] = pd.to_datetime(bios_new['born_date'])

bios_new['born_year'] = bios_new['dob'].dt.year

print(bios_new.query('first_name=="John"'))
bios_new.to_csv('./data/bios_new.csv')