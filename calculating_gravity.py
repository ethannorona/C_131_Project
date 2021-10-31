import pandas as pd

df = pd.read_csv('final_data.csv')

print(df.head())
print(df.columns)

df.drop(['Unnamed: 0'], axis = 1, inplace = True)
print(df.head())

print(df.dtypes)

df['Radius'] = df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = []

#converting solar mass and radius into km & kg
def convert_to_si(radius, mass):
    for i in range(0, len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30

convert_to_si(radius, mass)

def gravity_calculation(radius, mass):
    G = 6.674e-11
    for index in range(0, len(mass)):
        g = (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius, mass)

df["Gravity"] = gravity
print(df)

#df['Distance']=df['Distance'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df.to_csv("star_with_gravity.csv")
print(df.dtypes)


"""Tried a different way to have the code work but there was an issue with line 57"""
"""import csv
import pandas as pd

rows = []

with open("final_data.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
        
#headers = rows[0]
#star_data_rows = rows[1:]

rows[4] = rows[4].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = rows[4].to_list()
mass = rows[3].to_list()
gravity = []

#converting solar mass and radius into km & kg
def convert_to_si(radius, mass):
    for i in range(0, len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30

convert_to_si(radius, mass)

def gravity_calculation(radius, mass):
    G = 6.674e-11
    for index in range(0, len(mass)):
        g = (mass[index]*G)/((radius[index])**2)
        gravity.append(g)
        
gravity_calculation(radius, mass)

rows["Gravity"] = gravity

#rows['Distance']=rows['Distance'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
rows.to_csv("star_with_gravity.csv")"""