import csv
from plotly import offline

filename = 'data/wf_2020_01_14-21.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    # print(header)

    # with open('data/wf_2020_01_14-21_high_conf.csv', 'w') as hc:
    #     write_hc = csv.writer(hc)
    #     for row in reader:
    #         if int(row[8])>80:
    #             write_hc.writerow(row)

    lons, lats, frps = [], [], []
    for i, row in enumerate(reader):
        if int(row[8]) == 100:
            try:
                lons.append(float(row[1]))
                lats.append(float(row[0]))
                frps.append(float(row[11]))
            except ValueError:
                print('some data missing on row {}'.format(i))
    print(len(lons))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': frps,
    'marker': {
        'size': [frp/50 for frp in frps],
        'color': frps,
        'colorscale': 'YlOrRd',
        'colorbar': {'title': 'Fire Radiative Power (megawatts)'}
    },
}]

layout = {
    'title': 'World Fire (21-14, Jan, 2020)',
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='wf_map.html')