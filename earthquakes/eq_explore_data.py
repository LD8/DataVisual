import json

filename = 'data/eq_data_1_day_m1.json'
# open json file and load (actually load and save into a var)
with open(filename) as f:
    origin_file = json.load(f)

# ----------------- convert json into readable text ------------------ #
# readable_file = 'data/readable_eq_data.json'
# # open another file to dump (write data into file)
# with open(readable_file, 'w') as f:
#     json.dump(origin_file, f, indent=4)

# get data that only matter from the original data
all_features = origin_file['features']
# print(len(all_features))

mags, lons, lats = [], [], []

for feature in all_features:
    try:
        mags.append(feature['properties']['mag'])
        lons.append(feature['geometry']['coordinates'][0])
        lats.append(feature['geometry']['coordinates'][1])
    except:
        print('some data missing...')

print(mags[:10])
print(lons[:10])
print(lats[:10])
