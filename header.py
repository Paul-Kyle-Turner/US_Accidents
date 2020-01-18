"""US Accidents Headers
The US Accidents data contains 49 columns listed as a shortcut instead of reading the file every time for the
header strings.
"""

'''Header Listing
This constant listing gives the header for each column in the US Accidents data.
Each header element is a tuple consisting of the header string and the type used for that column.
'''
HEADER = [('ID', str), 
          ('Source', str), 
          ('TMC', float), 
          ('Severity', int), 
          ('Start_Time', str), 
          ('End_Time', str), 
          ('Start_Lat', float), 
          ('Start_Lng', float), 
          ('End_Lat', float), 
          ('End_Lng', float), 
          ('Distance(mi)', float), 
          ('Description', str), 
          ('Number', float), 
          ('Street', str), 
          ('Side', str), 
          ('City', str), 
          ('County', str), 
          ('State', str), 
          ('Zipcode', str), 
          ('Country', str), 
          ('Timezone', str), 
          ('Airport_Code', str), 
          ('Weather_Timestamp', str), 
          ('Temperature(F)', float), 
          ('Wind_Chill(F)', float), 
          ('Humidity(%)', float), 
          ('Pressure(in)', float), 
          ('Visibility(mi)', float), 
          ('Wind_Direction', str), 
          ('Wind_Speed(mph)', float), 
          ('Precipitation(in)', float), 
          ('Weather_Condition', str), 
          ('Amenity', bool), 
          ('Bump', bool), 
          ('Crossing', bool), 
          ('Give_Way', bool), 
          ('Junction', bool), 
          ('No_Exit', bool), 
          ('Railway', bool), 
          ('Roundabout', bool), 
          ('Station', bool), 
          ('Stop', bool), 
          ('Traffic_Calming', bool), 
          ('Traffic_Signal', bool), 
          ('Turning_Loop', bool), 
          ('Sunrise_Sunset', str), 
          ('Civil_Twilight', str), 
          ('Nautical_Twilight', str), 
          ('Astronomical_Twilight', str)]

__all__ = ["HEADER"]


# Header Fetch Script
if __name__ == "__main__":
    import pandas as pd
    
    def gather_data(file="data/US_Accidents_May19.csv"):
        with open(file, 'r+') as csv_file:
            data = pd.read_csv(csv_file, sep=',')
        return data.columns.values, data.to_numpy()

    header, data = gather_data()

    # Print Header Strings
    print(header.tolist())

    types = []
    for col in data.T:
        types.append(type(col[0]))
    
    # Print Data Types for each Column/Header
    print(types)

    print(list(map(lambda x, y: (x, y), header, types)))
