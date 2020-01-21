import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
# open json file and load (actually load and save into a var)
with open(filename) as f:
    origin_file = json.load(f)

# get data that only matter from the original data
all_features = origin_file['features']
# print(len(all_features))

mags, lons, lats, hover_titles = [], [], [], []

for feature in all_features:
    try:
        mags.append(feature['properties']['mag'])
        lons.append(feature['geometry']['coordinates'][0])
        lats.append(feature['geometry']['coordinates'][1])
        hover_titles(feature['properties']['title'])
    except:
        print('some data missing...')

# data = [Scattergeo(lon=lons, lat=lats)] # Scattergeo needs attributes lon=[] and lat=[]
# better customisation with syntax below:
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_titles,
    # the appearance of the graph highly depends on 'marker' property
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags, # a scale of color according to the scale of mags
        'colorscale': 'Viridis', # a color scheme from yellow to dark blue
        'reversescale': True, # otherwise the color scale is reversed
        'colorbar': {'title': 'Magnitude'},
    },
}]

layout = Layout(title='Earthquakes happened in 30 days') # Layout constructor needs attributes title=''
fig = {'data': data, 'layout': layout }
offline.plot(fig, filename='eq_world.map.html')

# 3.5h for a earphone
# 25% for each charge for the earphones
# 3.5*4=15h