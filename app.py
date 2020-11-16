# def find_top_confirmed(n = 15):

#     import pandas as pd
#     corona_df=pd.read_csv("covid.csv")
#     by_country = corona_df.groupby('Zipcode').sum()[['Description']]
#     cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
#     return cdf

# cdf=find_top_confirmed()
# pairs=[(country,confirmed) for country,confirmed in zip(cdf.index,cdf['Confirmed'])]


# import folium
# import pandas as pd
# corona_df = pd.read_csv("dataset.csv")
# corona_df=corona_df[['Lat','Long_','Confirmed']]
# corona_df=corona_df.dropna()

# m=folium.Map(location=[34.223334,-82.461707],
#             tiles='Stamen toner',
#             zoom_start=8)

# # def circle_maker(x):
# #     folium.Circle(location=[x[0],x[1]],
# #                  radius=float(x[2]),
# #                  color="red",
# #                  popup='confirmed cases:{}'.format(x[2])).add_to(m)
# # corona_df.apply(lambda x:circle_maker(x),axis=1)

# html_map=m._repr_html_()
# from flask import Flask,render_template

# app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html",table=cdf, cmap=html_map,pairs=pairs)

# if __name__=="__main__":
#     app.run(debug=True)


























# # import folium
# # import pandas as pd
# # # import requests
# # calls_df = pd.read_csv("covid.csv")


# # calls_df=calls_df.dropna()

# # m=folium.Map(location=[40.71427, -74.00597],
# #             tiles='Stamen toner',
# #             zoom_start=8)

# # def circle_maker(x):
# #     folium.Circle(location=[x[0],x[1]],
# #                  radius=float(x[2])*10,
# #                  color="red",
# #                  popup='{}\n Complaint Type:{}'.format(x[3],x[2])).add_to(m)
# #     calls_df[['Latitude','Longitude','Complaint Type']].apply(lambda x:circle_maker(x),axis=1)
# # html_map=m._repr_html_()


import folium
import requests
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask
from flask import render_template


df = pd.read_csv("complaint.csv")


#Zipcode user input goes here

df369 = df[df["IncidentZip"].isin([10005, 10065,11102,10474, 11369, 11211])]


m = folium.Map(location = [40.712776, -74.005974], zoom_start = 12)

#go through each complaint, make a circle, add to map

# Read up on pandas read sql. 
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html
#https://pythontic.com/pandas/serialization/mysql


#because our dataset is too large, I reduced the number of rows in the range
for i in range(0,len(df369)):
    folium.Circle(
        location=[df369.iloc[i]["Latitude"], df369.iloc[i]["Longitude"]],
        popup="Complaint Type: " + df369.iloc[i]["ComplaintType"]+ ", " + "Agency: " + df369.iloc[i]["AgencyName"],
        radius = 20,
    ).add_to(m)


html_map = m._repr_html_()


app = Flask(__name__)


@app.route("/index")
def home():
    return render_template("homepage.html", cmap=html_map)

# @app.route("/")
# def home():
#     return render_template("home.html", cmap = html_map)

if __name__ == "__main__":
    app.run(debug=True)