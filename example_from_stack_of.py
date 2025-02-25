import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.graph_objects as go

nomi = pgeocode.Nominatim('us')

edf = pd.read_csv('myFile.tsv', sep='\t',header=None, index_col=False ,names=['colC','zipcode','count'])
edf['Latitude'] = (nomi.query_postal_code(edf['zipcode'].tolist()).latitude)
edf['Longitude'] = (nomi.query_postal_code(edf['zipcode'].tolist()).longitude)

fig = go.Figure(data=go.Scattergeo(
        lon = edf['Longitude'],
        lat = edf['Latitude'],
        text = edf['colC'],
        mode = 'markers',
        marker_color = edf['count'],
        ))

fig.update_layout(
        title = 'colC Distribution',
        geo_scope='usa',
    )
fig.show()