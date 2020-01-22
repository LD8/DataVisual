import json, time
from plotly import offline

def eq_mapGenerator(json_file_path, target_html_filename):
    '''a function to generate visual representation of earthquakes from GeoJSON files'''

    with open(json_file_path) as f:
        original_data = json.load(f)

    # enable if geojson file is unreadable and you wish to read it
    # filename2 = 'data/eq_readable.json'
    # with open(filename2, 'w') as f:
    #     json.dump(original_data, f, indent=4)

    generated_time = original_data['metadata']['generated']/1000
    meta_time = time.strftime('%Y-%m-%d', time.localtime(generated_time-2592000))
    meta_title = original_data['metadata']['title'] + '\n(since ' + meta_time + ')'
    # print(meta_time, meta_title)

    features = original_data['features']
    mags, lons, lats, hover_titles = [], [], [], []

    for feature in features:
        mags.append(feature['properties']['mag'])
        hover_titles.append(feature['properties']['title'])
        lons.append(feature['geometry']['coordinates'][0])
        lats.append(feature['geometry']['coordinates'][1])

    data = {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_titles,
        'marker': {
            'size': [mag*5 for mag in mags],
            'color': mags,
            'opacity': 0.7,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {
                'title': 'Magnitude',
                'len': 0.5,
            },
        },
    }

    layout = {'title': meta_title,}

    fig = {'data': data, 'layout': layout}
    offline.plot(fig, filename=target_html_filename)

if __name__ == "__main__":
    json_file = str(input('Please enter a json file path: \n'))
    html_filename = str(input('Please enter a name for output html file: \n'))
    eq_mapGenerator(json_file, html_filename)