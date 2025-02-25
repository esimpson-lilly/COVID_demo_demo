import plotly.express as px
from urllib.request import urlopen
import json



response =  open('in_indiana_zip_codes_geo.min.json', 'r')
zipcodes = json.load(response)
fig = px.choropleth(df, 
                    geojson=zipcodes, 
                    locations='ZIP_Code', 
                    color='Cluster',
                    color_continuous_scale="Viridis",
                    range_color=(1,5),
                    featureidkey="properties.ZCTA5CE10",
                    scope="usa",
                    labels={'Cluster':'Cluster_Category'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})