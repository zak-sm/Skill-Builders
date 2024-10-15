from pathlib import Path
import json
import plotly.express as px


#Formatting the JSON file into a more readable format----------------------------------------------------------------
#Read data as a string and convert it to a python object
#path = Path('eq_data/eq_data_30_day_m1.geojson')
#contents = path.read_text()
#new_eq_data = json.loads(contents)

#Create a new and more readable version of the JSON data
#path = Path('eq_data/readable_30day_eq_data.geojson')
#eadable_contents = json.dumps(new_eq_data, indent=4)
#path.write_text(readable_contents)

#END FORMATTING -----------------------------------------------------------------------------------------------------

#Reimport data

path = Path('eq_data/readable_30day_eq_data.geojson')
contents = path.read_text()
eq_data = json.loads(contents)

#Examine all eq's as data sets

all_eq_dicts = eq_data['features']

lon, lat, mag, names = [], [], [], []

for quake in all_eq_dicts:
    try:
        long = quake['geometry']['coordinates'][0]
        lati = quake['geometry']['coordinates'][1]
        mags = quake['properties']['mag']
        name = quake['properties']['title']
    except ValueError:
        print(f'Missing data for quake at {name}')
    else:
        lon.append(long)
        lat.append(lati)
        mag.append(mags)
        names.append(name)


title = 'Global Earthquakes in the past 24 hours'
fig = px.scatter_geo(
    lon=lon,
    lat=lat,
    hover_name=names,
    title = title,
    size=mag, #adds magnitude as size of points
    color=mag, #tells python how to color the points based on their magnitude
    color_continuous_scale='agsunset',#adds a color scale to show differences in magnitude
    labels={'color':'Magnitude'}, #sets the color label as magnitude, its 'color' by default #only takes a dict as argument
    projection='natural earth'# modifies the base map to be rounded and shaped like a globe
    ,) 

fig.show()