
# Converts a single line in the source data file to a cleaned up dictionary
def line_to_dict(line):
    fields = line.split(",")

    return {
        'ID': fields[0],
        'Name': fields[1].strip(),
        'Date': fields[2],
        'Time': fields[3],
        'Status': fields[5].strip(),
        'Latitude': fields[6],
        'Longitude': fields[7],
        'MaximumWind': int(fields[8]),
    }

# Open the source data file, ignore the headers
with open('data/newatlantic.csv') as f:
    headers = f.readline()
    lines = f.read().split('\n')

#Build up a dictionary with the row containing the max wind speed for each storm
storms = {}
for line in lines:
    dict = line_to_dict(line)
    id = dict['ID']
    max = storms.get(id, dict)
    if dict['MaximumWind'] > max['MaximumWind']:
        max = dict
    storms[id] = max


with open('storms.csv', 'w') as f:
    f.write('ID,Name,Date,Time,Status,Latitude,Longitude,MaximumWind\n')
    for storm in storms.values():
        str = "{0},{1},{2},{3},{4},{5},{6},{7}\n".format(storm['ID'], storm['Name'], storm['Date'], storm['Time'], storm['Status'], storm['Latitude'], storm['Longitude'], storm['MaximumWind'])
        f.write(str)

