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


# bios = pd.read_csv("./data/bios.csv")
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


# bios_new = bios.copy()
# bios_new['first_name']= bios_new['name'].str.split(' ').str[0]
# bios_new.index = bios['athlete_id']
# bios_new.drop(columns='athlete_id', inplace=True)
# bios_new['dob'] = pd.to_datetime(bios_new['born_date'])

# bios_new['born_year'] = bios_new['dob'].dt.year

# print(bios_new.query('first_name=="John"'))
# bios_new.to_csv('./data/bios_new.csv')

# bios['height_category'] = bios['height_cm'].apply(lambda x: "Short" if x <165 else ('Average' if x<185 else 'Tall') ) #the use of apply with lambda function to create new column based on condition
# print(bios.query('height_category == "Short"'))
#remember the syntax of nested if else in lambda function is: value_if_true if condition else (value_if_true2 if condition2 else value_if_false2)

# bios['weight_category'] = bios['weight_kg'].apply(lambda x:'Heavy Weight' if x>90 else 'Light Weight')
# print(bios[["name", "NOC","weight_kg"]].query('weight_kg>90'))

# def categorize_athelete(row):
#     if row['height_cm']<175 and row['weight_kg']<70:
#         return 'Lightweight'
#     elif row['height_cm']<185 and row['weight_kg']<= 85:
#         return 'Middleweight'
#     else:
#         return 'Heavyweight'
#     #we can also use row.height_cm instead of row['height_cm']

# bios['Category'] = bios.apply(categorize_athelete, axis=1) #note that axis=1 means we are applying the function row wise if axis=0 then it would be column wise
# print(bios[['name','height_cm','weight_kg','Category']].head())



























# #### MERGING AND CONCATENATING

# nocs = pd.read_csv('./data/noc_regions.csv')
# # print(nocs.head())
# bios_new=pd.merge(bios,nocs, left_on='born_country',right_on='NOC', how='left')
# #left_on and right_on are used when the column names are different in both dataframes for merging
# bios_new.rename(columns={'region':'born_country_full'}, inplace=True)
# # print(bios_new[['name','born_country','born_country_full']].head())


# # usa = bios[bios['born_country']=='USA'].copy()
# # gbr = bios[bios['born_country']=='GBR'].copy()

# # new_df = pd.concat([usa,gbr])
# # print(new_df[['name', 'born_country']].sample(15))


# results = pd.read_csv('./data/results.csv')
# print(results[results['medal']=='Gold'].head())
# # print(bios.info())
# # Correct filtering: use .isin() to produce a boolean Series for row-wise filtering
# combined_df = pd.merge(results[results['medal'].isin(['Gold', 'Silver', 'Bronze'])], bios, on='athlete_id', how='left')
# print(combined_df[['athlete_id', 'name','year','discipline','event','medal']].sample(10))


























#### HANDLING NAN VALUES

# coffee = pd.read_csv('./warmup-data/coffee.csv')

# coffee.loc[[0,1],'Units Sold'] = np.nan
# print(coffee['Units Sold'].isna()) #this just returns boolean so we print only ones with NaN by following:
# print(coffee[coffee['Units Sold'].isna()])
# print(coffee.isna().sum())
# coffee.fillna("A number")a general solution may also be to replace it with coffee['Units Sold'].mean()
# coffee["Units Sold"].interpolate(). #works just like hoe the "+" thingy works in excel
# coffee.dropna(). #drops the full entire row for specific we can do coffee.dropna(subset=["Units Sold"])































###### AGGREGATING DATA
# bios  = pd.read_csv('./data/bios.csv')

# print(bios.head())
# print(bios[bios['born_country']=='USA']['born_region'].value_counts())

# coffee = pd.read_csv('./warmup-data/coffee.csv')
# print(coffee.groupby(["Coffee Type"])['Units Sold'].mean()) #So the function of groupby is to like whenever we compare the like sum thingy or mean thingy of all the rows it gives classficiation based on likeyeah try to understand it utsab

# coffee['Price'] = np.where(coffee["Coffee Type"]=="Latte",5.99,3.99)
# coffee["Revenue"] = coffee["Price"] * coffee["Units Sold"]
# print(coffee.info())

# print(coffee.groupby(["Coffee Type"]).agg({"Units Sold":"sum","Price":"mean"}))
# print(coffee.groupby(["Day"]).agg({"Revenue":"sum"}))
# pivot = coffee.pivot(columns='Coffee Type', index='Day', values='Revenue')
# print(pivot.loc['Monday'])

































####ADVANCED FUNCTIONALITY

# coffee['yesterday_revenue'] = coffee["Revenue"].shift(2)        #gives the previous value pf shift like we take a certain column anf then do .shift("No. we want of prev data") this particular exmaple does just the prev revenue
# coffee['pct_change'] = (coffee['Revenue']  - coffee["yesterday_revenue"] )/coffee["Revenue"] *100

# bios['height_rank'] = bios["height_cm"].rank()
# print(bios[["name", "height_cm", "height_rank"]].sort_values(["height_rank"],ascending=False))

# coffee["Cum_revenue"]=coffee["Revenue"].cumsum()
# coffee["3day_rev"] = coffee.groupby("Coffee Type")['Units Sold'].rolling(3).sum().reset_index(level=0,drop=True)
# print(coffee) 



###NOTE THAT THERE'S THIS NEW BACKEND FOUNDATION FOR PANDAS CALLED OYARROW AND IT HAS UPOPER HAND IN BEING RATHER EFFICIENT AND SUPPORTING SPECIIFC OPERATIONS LIKE STRING AND ALL 

