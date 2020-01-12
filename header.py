"""US Accidents Headers
The US Accidents data contains 49 columns listed as a shortcut instead of reading the file every time for the
header strings.
"""

'''Header Listing
This constant listing gives the header for each column in the US Accidents data.
'''
HEADER = ['ID',
          'Source', 
          'TMC', 
          'Severity', 
          'Start_Time', 
          'End_Time', 
          'Start_Lat', 
          'Start_Lng', 
          'End_Lat', 
          'End_Lng', 
          'Distance(mi)', 
          'Description', 
          'Number', 
          'Street', 
          'Side', 
          'City', 
          'County', 
          'State', 
          'Zipcode', 
          'Country', 
          'Timezone', 
          'Airport_Code', 
          'Weather_Timestamp', 
          'Temperature(F)', 
          'Wind_Chill(F)', 
          'Humidity(%)', 
          'Pressure(in)', 
          'Visibility(mi)', 
          'Wind_Direction', 
          'Wind_Speed(mph)', 
          'Precipitation(in)', 
          'Weather_Condition', 
          'Amenity', 
          'Bump', 
          'Crossing', 
          'Give_Way', 
          'Junction', 
          'No_Exit', 
          'Railway', 
          'Roundabout', 
          'Station', 
          'Stop', 
          'Traffic_Calming', 
          'Traffic_Signal', 
          'Turning_Loop', 
          'Sunrise_Sunset', 
          'Civil_Twilight', 
          'Nautical_Twilight', 
          'Astronomical_Twilight']

__all__ = ["HEADER"]


if __name__ == "__main__":
    import pandas as pd
    
    def gather_data(file="data/US_Accidents_May19.csv"):
        with open(file, 'r+') as csv_file:
            data = pd.read_csv(csv_file, sep=',', nrows=2)
        return data.columns.values, data

    header, _ = gather_data()
    print(header.tolist())
