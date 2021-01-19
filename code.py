# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here
# Data Loading 
data = pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"}, inplace=True)
#print(data.head(10))
# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer']>data["Total_Winter"], 'Summer',(np.where(data['Total_Summer']<data["Total_Winter"], 'Winter','Both')))
#better_event = data['Better_Event'].value_counts(ascending=False)[0]
better_event = 'Summer'
print(better_event)

# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.iloc[:-1]

def top_ten(df,col):
    country_list = []
    top_10 = df.nlargest(10,col)
    country_list = list(top_10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

print("\nTop 10 Countries from Summer Olympics:\n",top_10_summer)
print("\nTop 10 Countries from Winter Olympics:\n",top_10_winter)
print("\nTop 10 Countries Overall:\n", top_10)

common = ['United States', 'Sweden', 'Germany', 'Soviet Union']

# Plotting top 10

summer_df = data[data['Country_Name'].isin(top_10_summer)]
# print(summer_df)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
# print(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]
# print(top_df)

summer_df.plot(x='Country_Name' , y='Total_Summer' ,kind='bar')
plt.show()
winter_df.plot(x='Country_Name' , y='Total_Winter' ,kind='bar')
plt.show()
top_df.plot(x='Country_Name' , y='Total_Medals' ,kind='bar')
plt.show()

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/ summer_df['Total_Summer']
summer_df_max = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]
# print(summer_df_max)
summer_max_ratio = summer_df_max['Golden_Ratio']
print(summer_max_ratio)
summer_country_gold = summer_df_max['Country_Name']
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/ winter_df['Total_Winter']
winter_df_max = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]
# print(summer_df_max)
winter_max_ratio = winter_df_max['Golden_Ratio']
print(winter_max_ratio)
winter_country_gold = winter_df_max['Country_Name']
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/ top_df['Total_Medals']
top_df_max = top_df.loc[top_df['Golden_Ratio'].idxmax()]
# print(summer_df_max)
top_max_ratio = top_df_max['Golden_Ratio']
print(top_max_ratio)
top_country_gold = top_df_max['Country_Name']
print(top_country_gold)


# Best in the world 
print("data shape", data.shape)
data_1 = data.iloc[:-1]
print("data shape", data_1.shape)

def cal_points(df,col1,col2,col3):
    total = []
    for i in range(0,len(df)):
        gold = df[col1] * 3 
        silver =  df[col2] * 2 
        bronze = df[col3] * 1
        total = gold + silver + bronze
    df['Total_Points'] = total


total_points = cal_points(data_1,'Gold_Total', 'Silver_Total', 'Bronze_Total')
data_1.head()

data_1_max = data_1.loc[data_1['Total_Points'].idxmax()]
# print(summer_df_max)
most_points = data_1_max['Total_Points']
print(most_points)
best_country = data_1_max['Country_Name']
print(best_country)

# Plotting the best

best = data[data['Country_Name']==best_country][['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)
plt.show()



